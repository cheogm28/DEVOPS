import uvicorn
from fastapi import FastAPI
from app.api.v1.actions import router as actions_router


app = FastAPI()
app.include_router(actions_router,prefix="/actions", tags=["actions"])

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
