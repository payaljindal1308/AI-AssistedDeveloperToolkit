
# app/routers/__init__.py
from fastapi import APIRouter
from .collections import router as collections_router

router = APIRouter()
router.include_router(collections_router, prefix="/collections", tags=["collections"])