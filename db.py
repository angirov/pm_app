from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://postgres:pw@localhost:5432/project_tracker2')
Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(length=50))

    def __repr__(self) -> str:
        return f"<Project(project_id={self.project_id}, title={self.project_name})>"
    
class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    task_description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self) -> str:
        return f"<Task(task_id={self.task_id}, task_description={self.task_description})>"

Base.metadata.create_all(engine)

def create_session():
    session = sessionmaker(bind=engine)
    return session()

if __name__ == "__main__":
    session = create_session()

    clean_house = Project(project_name="Clean House Test")
    session.add(clean_house)
    session.commit()

