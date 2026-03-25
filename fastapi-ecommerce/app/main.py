from dotenv import load_dotenv
import os
import datetime
import uuid

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from service.products import add_product, get_all_products, remove_product, change_product
from schema.product import product, ProductUpdate


load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    DB_PATH = os.getenv("BASE_URL")
    # return {"message": "this is fasapi server", "data_path": DB_PATH}
    return JSONResponse(
        status_code= 200,
        content= {"message": "this is fasapi server", "data_path": DB_PATH}
    )

# @app.get('/products')
# def get_products():
#     return get_all_products()


@app.get("/products")
def list_products( 
    Name: str = Query(
        default=None, 
        min_length=1,
        max_length=50,
        examples=["Realme"],
        description="Name of the product to search for"),
    sort_by_price: bool = Query(
        default=False, 
        description="Whether to sort products by price"),
    order: str = Query(
        default="asc", 
        description="sort order by (asc or desc)"),
    limit: int = Query(
        default=10, 
        ge=1, 
        le=50, 
        description="Maximum number of products to return"),
                   
    offset: int = Query(
        default=0, 
        ge=0, 
        description="Number of products to skip")
        ):
    products = get_all_products()

    if Name:
        needle = Name.lower().strip()
        products = [p for p in products if needle in p.get("name", "").lower()]
    if not products:
        raise HTTPException(status_code=404, detail=f"no products found with name containing '{Name}'")
    
    
    if sort_by_price:
        reverse = order == "desc"
        products.sort(key=lambda p: p.get("price",0), reverse=reverse)
    total = len(products)
    products = products[offset:offset+limit]
    return {"total": total,"limit": limit,"offset": offset,"items": products}


@app.get("/products/{product_id}")
def get_product_by_id(product_id: str = Path(
    ...,
    min_length=36,
    max_length=36,
    examples=["2e64ac5f-5859-4212-a0e8-36b8a42844ad"],
    description="UUID of the product to retrieve")
    ):
    products = get_all_products()
    for product in products:
        if product.get("id") == product_id:
            return product
    raise HTTPException(status_code=404, detail=f"product with id '{product_id}' not found")


@app.post("/products", status_code=201)
def create_product(product: product):
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid.uuid4())
    product_dict["created_at"] = datetime.datetime.utcnow().isoformat() + "Z"
    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product.model_dump(mode="json")


@app.delete("/products/{product_id}")
def delete_product(product_id: uuid.UUID = Path( ..., description="UUID of the product to delete")):
    try:
        res = remove_product(str(product_id))
        return res
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.put("/products/{product_id}")
def update_product(
    product_id: uuid.UUID = Path(..., description="Product UUID"),
    payload: ProductUpdate = ...,):
    try:
        update_product = change_product(
            str(product_id), payload.model_dump(mode="json", exclude_unset=True)
        )
        return update_product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
