from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.ProfileType)
def create_profile_type(profile_type: schemas.ProfileTypeCreate, db: Session = Depends(get_db)):
    """
    Create a new profile_type.
    """
    db_profile_type = models.ProfileType(**profile_type.model_dump())
    db.add(db_profile_type)
    db.commit()
    db.refresh(db_profile_type)
    return db_profile_type


@router.get("/{profile_type_id}", response_model=schemas.ProfileType)
def read_profile_type(profile_type_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific profile_type by its ID.
    """
    db_profile_type = db.query(models.ProfileType).filter(models.ProfileType.id == profile_type_id).first()
    if db_profile_type is None:
        raise HTTPException(status_code=404, detail="ProfileType not found")
    return db_profile_type


@router.get("/", response_model=List[schemas.ProfileType])
def read_profile_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of profile_types.
    """
    profile_types = db.query(models.ProfileType).offset(skip).limit(limit).all()
    return profile_types


@router.put("/{profile_type_id}", response_model=schemas.ProfileType)
def update_profile_type(profile_type_id: int, profile_type: schemas.ProfileTypeUpdate, db: Session = Depends(get_db)):
    """
    Update a specific profile_type by its ID.
    """
    db_profile_type = db.query(models.ProfileType).filter(models.ProfileType.id == profile_type_id).first()
    if db_profile_type is None:
        raise HTTPException(status_code=404, detail="ProfileType not found")
    for key, value in profile_type.model_dump(exclude_unset=True).items():
        setattr(db_profile_type, key, value)
    db.add(db_profile_type)
    db.commit()
    db.refresh(db_profile_type)
    return db_profile_type


@router.delete("/{profile_type_id}", response_model=schemas.ProfileType)
def delete_profile_type(profile_type_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific profile_type by its ID.
    """
    db_profile_type = db.query(models.ProfileType).filter(models.ProfileType.id == profile_type_id).first()
    if db_profile_type is None:
        raise HTTPException(status_code=404, detail="ProfileType not found")
    db.delete(db_profile_type)
    db.commit()
    return db_profile_type
