from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from database import get_db
import models
import schemas

router = APIRouter()

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility function to hash passwords
def hash_password(password: str):
    return pwd_context.hash(password)

# Utility function to verify passwords
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # TODO: Implement token generation logic (e.g., using JWT)
    return {"access_token": user.username, "token_type": "bearer"}


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    hashed_password = hash_password(user.password)
    db_user = models.User(
        name=user.name,
        firstname=user.firstname,
        email=user.email,
        telegram=user.telegram,
        username=user.username,
        password=hashed_password,
        user_type=user.user_type,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific user by their ID.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of users.
    """
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """
    Update a specific user by their ID.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump(exclude_unset=True).items():
        if key == "password":
            value = hash_password(value)
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific user by their ID.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user
