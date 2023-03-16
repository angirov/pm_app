# ORM for an existing postgres db

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine('postgresql://wo:pw@localhost:5432/project_tracker')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Access the mapped classes
Projects = Base.classes.projects
Tasks = Base.classes.tasks

# Use the mapped classes to query the database
session = Session(engine)
projects = session.query(Projects).all()
for project in projects:
    print(project.project_name)