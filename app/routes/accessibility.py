from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def accessibility_options():
    return {
        "high_contrast": True,
        "text_to_speech": False,
        "keyboard_navigation": True
    }
