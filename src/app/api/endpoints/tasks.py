from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    bid = db.query(models.Bid).filter(models.Bid.id == task.bid_id).first()
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    product = db.query(models.Product).filter(models.Product.id == task.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    material = db.query(models.Material).filter(models.Material.id == task.material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")

    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific task by its ID.
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of tasks.
    """
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """
    Update a specific task by its ID.
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific task by its ID.
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return db_task
