from app.ext.database import db
from app.models import Product


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Product(id=1, name="Ciabatta", price="5", description="Italian Bread"),
        Product(id=2, name="Baguete", price="5", description="French Bread"),
        Product(id=3, name="Pretzel", price="5", description="German Bread"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))