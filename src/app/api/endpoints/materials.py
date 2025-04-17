from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    """
    Create a new material.
    """
    db_material = models.Material(**material.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


@router.get("/{material_id}", response_model=schemas.Material)
def read_material(material_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific material by its ID.
    """
    db_material = db.query(models.Material).filter(models.Material.id == material_id).first()
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@router.get("/", response_model=List[schemas.Material])
def read_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of materials.
    """
    materials = db.query(models.Material).offset(skip).limit(limit).all()
    return materials


@router.put("/{material_id}", response_model=schemas.Material)
def update_material(material_id: int, material: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    """
    Update a specific material by its ID.
    """
    db_material = db.query(models.Material).filter(models.Material.id == material_id).first()
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    for key, value in material.model_dump(exclude_unset=True).items():
        setattr(db_material, key, value)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


@router.delete("/{material_id}", response_model=schemas.Material)
def delete_material(material_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific material by its ID.
    """
    db_material = db.query(models.Material).filter(models.Material.id == material_id).first()
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(db_material)
    db.commit()
    return db_material
