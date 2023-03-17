from app import app, db, Author, Paper
from sqlalchemy.exc import IntegrityError

class DbConnector():
    def __init__(self):
        app.app_context().push()
        self.session = db.session

    def add_object(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
            return True
        except IntegrityError as e:
            self.session.rollback()
            print(e)
            return False

    def add_author(self, name):
        author = Author(name=name)
        if self.add_object(author):
            author_id = Author.query.filter_by(name=name).first().id
            return author_id
        else:
            return -1

    def add_paper(self, id, text, author_id):
        paper = Paper(id=id, text=text, author_id=author_id)
        self.add_object(paper)
        pass