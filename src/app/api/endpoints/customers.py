from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.
    """
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific customer by its ID.
    """
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.get("/", response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of customers.
    """
    customers = db.query(models.Customer).offset(skip).limit(limit).all()
    return customers


@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    """
    Update a specific customer by its ID.
    """
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer.model_dump(exclude_unset=True).items():
        setattr(db_customer, key, value)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.delete("/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific customer by its ID.
    """
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return db_customer
