from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proj.sqlite" # 'sqlite:///' + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())

    def __repr__(self) -> str:
        return f"<Project: {self.name}>"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    project = db.relationship("Project")
    created_at = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())

    def __repr__(self) -> str:
        return f"<Task: {self.discription}>"


@app.route("/")
def show_project():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project_id=project_id)

@app.route("/add/project", methods=["POST"])
def add_project():
    # Add project
    return "Project added successfully!"

@app.route("/add/task/<project_id>",methods=["POST"])
def add_task(project_id):
    #Add project
    return f"Taks added successfully to Project {project_id}!"

