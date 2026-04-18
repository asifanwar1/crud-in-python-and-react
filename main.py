from fastapi import FastAPI
from models import Product
from database import session

app = FastAPI()


@app.get("/")
def greet():
    return "Hello, World!"


products = [
    Product(id=1, name="Phone", description="Description for phone",
            price=10.0, quantity=5),
    Product(id=2, name="Laptop", description="Description for laptop",
            price=20.0, quantity=3),
    Product(id=3, name="Tablet", description="Description for tablet",
            price=15.0, quantity=7)
]


@app.get("/products")
def get_all_products():
    db = session()
    db.query(Product).all()
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return product
    return {"error": "Product not found"}


@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            deleted_product = products.pop(i)
            return deleted_product
    return {"error": "Product not found"}
