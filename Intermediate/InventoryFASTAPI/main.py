from fastapi import FastAPI
from Database import Database
from Inventory_mana import InventoryManager
from API_Routes import router
import uvicorn

api = FastAPI()
api.include_router(router)