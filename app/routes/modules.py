from fastapi import APIRouter
from app.core.module_loader import _MODULE_MANIFEST

router = APIRouter()

@router.get("/")
def list_modules():
    return _MODULE_MANIFEST
