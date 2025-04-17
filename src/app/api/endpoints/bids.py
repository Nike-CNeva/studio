from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas


router = APIRouter()


@router.post("/", response_model=schemas.Bid)
def create_bid(bid: schemas.BidCreate, db: Session = Depends(get_db)):
    """
    Create a new bid.
    """
    customer = db.query(models.Customer).filter(models.Customer.id == bid.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db_bid = models.Bid(**bid.model_dump())
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid


@router.get("/{bid_id}", response_model=schemas.Bid)
def read_bid(bid_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific bid by its ID.
    """
    db_bid = db.query(models.Bid).filter(models.Bid.id == bid_id).first()
    if db_bid is None:
        raise HTTPException(status_code=404, detail="Bid not found")
    return db_bid


@router.get("/", response_model=List[schemas.Bid])
def read_bids(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of bids.
    """
    bids = db.query(models.Bid).offset(skip).limit(limit).all()
    return bids


@router.put("/{bid_id}", response_model=schemas.Bid)
def update_bid(bid_id: int, bid: schemas.BidUpdate, db: Session = Depends(get_db)):
    """
    Update a specific bid by its ID.
    """
    db_bid = db.query(models.Bid).filter(models.Bid.id == bid_id).first()
    if db_bid is None:
        raise HTTPException(status_code=404, detail="Bid not found")
    for key, value in bid.model_dump(exclude_unset=True).items():
        setattr(db_bid, key, value)
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid


@router.delete("/{bid_id}", response_model=schemas.Bid)
def delete_bid(bid_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific bid by its ID.
    """
    db_bid = db.query(models.Bid).filter(models.Bid.id == bid_id).first()
    if db_bid is None:
        raise HTTPException(status_code=404, detail="Bid not found")
    db.delete(db_bid)
    db.commit()
    return db_bid
