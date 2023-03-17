from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proj.sqlite" # 'sqlite:///' + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())

    def __repr__(self) -> str:
        return f"<Author: {self.name}>"

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author")
    created_at = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())

    def __repr__(self) -> str:
        return f"<Paper: {self.discription}>"


@app.route("/")
def show_author():
    authors = Author.query.all()
    return render_template("index.html", authors=authors)

@app.route("/author/<author_id>")
def show_paper(author_id):
    return render_template("author-paper.html", author_id=author_id)

@app.route("/add/author", methods=["POST"])
def add_author():
    # Add author
    return "Author added successfully!"

@app.route("/add/task/<author_id>",methods=["POST"])
def add_task(author_id):
    #Add author
    return f"Taks added successfully to Author {author_id}!"

