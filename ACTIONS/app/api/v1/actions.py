from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_actions():
    return {"message": "List of actions"}



