from app import app, db, Author, Paper

app.app_context().push()

a = Author(name="Vova")
db.session.add(a)

p = Paper(text="hello world", author=a.id)
db.session.add(p)

db.session.commit()