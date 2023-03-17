from app import app, db, Author, Paper

app.app_context().push()
db.create_all()