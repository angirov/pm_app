from app import app, db
from sqlalchemy.exc import IntegrityError

class DbConnector():
    def __init__(self, app, db):
        app.app_context().push()
        self.session = db.session

    def add_object(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()
            print(e)