import os
from typing import List, Dict
from tqdm import tqdm
import pandas as pd
import pickle
from Bio import Entrez

from db_connector import DbConnector

class Crawler():


    def __init__(self, 
                 init_names: List[str], 
                 email: str,
                 data_dir: str = "data",
                 done_path: str = "done_list.pkl",
                 max_authors: int = 100,
                ) -> None:
        self.db = "pubmed"
        self.done_path = done_path
        self.names = init_names
        self.data_dir = data_dir
        self.max_authors = max_authors
        self.done = []
        self.dbcon = DbConnector()
        Entrez.email = email

    def add_coauthors_to_names(self, coauthors_dict: Dict[str, int]):
        lst = list(coauthors_dict.keys())
        for name in lst:
            if name not in self.names:
                self.names += [name]
        pass


    def crawl(self):
        counter = 0
        for name in self.names:
            if name not in self.done and counter < self.max_authors:
                print(f">>> Loading {name}'s coauthors")
                coauthors_dict = self.get_coauthors(name)
                self.add_coauthors_to_names(coauthors_dict)
                if self.save_coauthors(name, coauthors_dict):
                    print(f">>> {name}'s coauthors saved!")
                    self.done += [name]
                    counter += 1
                else:
                    print(f">>> Failed to save {name}!")
        with open(self.done_path, "wb") as file:
            pickle.dump(self.done, file)
        print(f">>> Crawled over {len(self.done)} authors")


    def get_authors_pmids(self, name: str) -> List[str]:
        handle = Entrez.esearch(db="pubmed", term=name, retmax=10000)
        record = Entrez.read(handle)
        ids = record["IdList"]
        return ids


    def get_abstract(self, id: str) -> str:
        handle = Entrez.efetch(db=self.db, 
                                        id=id, 
                                        retmode="text", 
                                        rettype="abstract")
        abstract_text = handle.read()
        return abstract_text


    def get_abstracts(self, ids: List[str]) -> List[str]:
        abstracts = []
        for id in tqdm(ids):
            abstract_text = self.get_abstract(id)
            abstracts += [abstract_text]
        return abstracts


    def get_paper_authors(self, id: str,) -> List[str]:
        authors = []
        handle = Entrez.esummary(db=self.db, id=id, retmode="xml")
        records = Entrez.parse(handle)
        for record in records:
            # each record is a Python dictionary or list.
            authors +=  record['AuthorList']
        return authors


    def get_coauthors(self, name: str) -> Dict[str, int]:
        pmids = self.get_authors_pmids(name)
        coauthors = {}
        for id in tqdm(pmids):
            authors = self.get_paper_authors(id)
            for author in authors:
                if author != name:
                    if author in coauthors:
                        coauthors[author] += 1
                    else:
                        coauthors[author] = 1
        return coauthors
    
    def save_coauthors(self, author_name: str, coauthors: Dict[str, int]) -> bool:
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        df = pd.DataFrame.from_dict(coauthors, orient='index')
        df.sort_values(by=0, ascending=False)
        filename = author_name.replace(" ", "_")
        df.to_pickle(self.data_dir + "/coauthors_" + filename + ".pkl")
        return True

    def add_author(self, name):
        print(f"Collecting papers by {name}", type(name))
        ids = self.get_authors_pmids(name)
        author_id = self.dbcon.add_author(name)
        if author_id >= 0:
            abstracts = self.get_abstracts(ids)
            for paper_id, abstract in zip(ids, abstracts):
                self.dbcon.add_paper(paper_id, abstract, author_id)
                print(f"Added {paper_id}: {abstract[:10]}")
        else:
            print(">>> Failure!!!")