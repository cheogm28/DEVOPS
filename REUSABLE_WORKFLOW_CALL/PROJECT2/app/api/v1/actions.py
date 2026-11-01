from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_actions():
    return {"This change triggers an action in Project 2"}



