from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from flask import current_app

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # tasks

    def __repr__(self) -> str:
        return f"<Project: {self.name}>"


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    discription = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project")

    def __repr__(self) -> str:
        return f"<Task: {self.discription}>"