from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

@router.get("/")
def get_strings(lang: str = "en"):
    path = Path(f"app/i18n/strings_{lang}.json")
    if not path.exists():
        return {"error": "Language not found"}
    return json.loads(path.read_text(encoding="utf-8"))
