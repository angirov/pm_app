from app import app, db, Author, Paper
from sqlalchemy.exc import IntegrityError
from db_connector import DbConnector

name="Pupu2"

dc = DbConnector()
a = Author(name=name)

author_id = dc.add_object(a)

author_id = Author.query.filter_by(name="Pupu2").first().id

dc.add_paper(id="9876986865876", text="hello world!!22222", author_id=str(author_id))
print(">>>>>>>>>> done!")