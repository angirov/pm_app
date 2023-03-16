from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

dbname = "projects.sqlite"

engine = create_engine("sqlite:///" + dbname)

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    discription = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", backref=backref("tasks", order_by=id))

Base.metadata.create_all(engine)