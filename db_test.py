from app import app, db, Author, Paper
from sqlalchemy.exc import IntegrityError
from db_connector import DbConnector

dc = DbConnector(app, db)
a = Author(name="Pupu2")

dc.add_object(a)

a = Author.query.filter_by(name="Pupu2").first()

p = Paper(text="hello world!!22222", author_id=a.id)
dc.add_object(p)

print(">>>>>>>>>> done!")