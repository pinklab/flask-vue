from server.ext.database import db
from server.models import Task


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Task(id=1, name="Study", description="python and flask"),
        Task(id=2, name="Work", description="add feature"),
        Task(id=3, name="Buy food", description="pizza"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Task.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
