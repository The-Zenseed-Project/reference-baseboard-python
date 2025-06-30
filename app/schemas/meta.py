from pydantic import BaseModel
from typing import Dict

class MetaInfo(BaseModel):
    app_name: str
    version: str
    modules: Dict[str, str]
