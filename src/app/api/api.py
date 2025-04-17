from fastapi import FastAPI

from database import engine
import models
from app.api.endpoints import users, bids, tasks, products, materials, files, profile_types

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(bids.router, prefix="/bids", tags=["bids"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(materials.router, prefix="/materials", tags=["materials"])
app.include_router(files.router, prefix="/files", tags=["files"])
app.include_router(profile_types.router, prefix="/profile-types", tags=["profile_types"])
