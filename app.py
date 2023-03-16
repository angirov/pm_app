from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://wo:pw@localhost:5432/project_tracker'


@app.route("/")
def show_project():
    return render_template("index.html")

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

app.run(debug=True, host="localhost", port=3000)