from .models import Product

def get_all(db):
    return db.query(Product).all()

def create(db, data):
    p = Product(**data)
    db.add(p)
    db.commit()
