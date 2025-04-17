from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.Files)
def create_file(file: schemas.FilesCreate, db: Session = Depends(get_db)):
    """
    Create a new file.
    """
    db_file = models.Files(**file.model_dump())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


@router.get("/{file_id}", response_model=schemas.Files)
def read_file(file_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific file by its ID.
    """
    db_file = db.query(models.Files).filter(models.Files.id == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file


@router.get("/", response_model=List[schemas.Files])
def read_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of files.
    """
    files = db.query(models.Files).offset(skip).limit(limit).all()
    return files


@router.put("/{file_id}", response_model=schemas.Files)
def update_file(file_id: int, file: schemas.FilesUpdate, db: Session = Depends(get_db)):
    """
    Update a specific file by its ID.
    """
    db_file = db.query(models.Files).filter(models.Files.id == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    for key, value in file.model_dump(exclude_unset=True).items():
        setattr(db_file, key, value)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


@router.delete("/{file_id}", response_model=schemas.Files)
def delete_file(file_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific file by its ID.
    """
    db_file = db.query(models.Files).filter(models.Files.id == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    db.delete(db_file)
    db.commit()
    return db_file
