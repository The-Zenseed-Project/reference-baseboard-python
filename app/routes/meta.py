from fastapi import APIRouter
from app.schemas.meta import MetaInfo
from app.core.module_loader import get_module_versions

router = APIRouter()

@router.get("/", response_model=MetaInfo)
def meta_info():
    return MetaInfo(
        app_name="Zenseed Baseboard",
        version="0.1.0",
        modules=get_module_versions()
    )
