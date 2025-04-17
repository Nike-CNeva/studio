from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product.
    """
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific product by its ID.
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.get("/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of products.
    """
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    """
    Update a specific product by its ID.
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific product by its ID.
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return db_product
