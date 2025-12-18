from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import OperationalError
import time

from .database import SessionLocal, engine, Base
from .models import Product

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    retries = 10
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Base de datos lista")
            break
        except OperationalError:
            retries -= 1
            print("⏳ Esperando MySQL...")
            time.sleep(3)
    else:
        raise RuntimeError("❌ No se pudo conectar a MySQL")

@app.get("/")
def list_products(request: Request):
    db = get_db()
    products = db.query(Product).all()
    return templates.TemplateResponse(
        "products.html",
        {"request": request, "products": products}
    )

@app.get("/products/new")
def new_product(request: Request):
    return templates.TemplateResponse(
        "product_form.html",
        {"request": request, "product": None}
    )

@app.post("/products/new")
def create_product(
    name: str = Form(...),
    description: str = Form(""),
    price: float = Form(...)
):
    db = get_db()
    product = Product(name=name, description=description, price=price)
    db.add(product)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/products/edit/{product_id}")
def edit_product(product_id: int, request: Request):
    db = get_db()
    product = db.get(Product, product_id)
    return templates.TemplateResponse(
        "product_form.html",
        {"request": request, "product": product}
    )

@app.post("/products/edit/{product_id}")
def update_product(
    product_id: int,
    name: str = Form(...),
    description: str = Form(""),
    price: float = Form(...)
):
    db = get_db()
    product = db.get(Product, product_id)
    product.name = name
    product.description = description
    product.price = price
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/products/delete/{product_id}")
def delete_product(product_id: int):
    db = get_db()
    product = db.get(Product, product_id)
    db.delete(product)
    db.commit()
    return RedirectResponse("/", status_code=303)
