from app import app, db, Author, Paper
from sqlalchemy.exc import IntegrityError

app.app_context().push()

a = Author(name="Pupu2")

def db_add_object(obj):
    try:
        db.session.add(obj)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(e)

db_add_object(a)

a = Author.query.filter_by(name="Pupu2").first()

p = Paper(text="hello world!!22222", author_id=a.id)
db.session.add(p)
db.session.commit()

print(">>>>>>>>>> done!")