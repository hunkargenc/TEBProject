from __future__ import annotations

from fastapi import APIRouter, Depends

from app.apis.api_v1.prediction import sentiment_prediction as sentiment_func
from app.apis.api_v1.prediction import intention_prediction as intention_func
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of TEB Project FastAPI. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.get("/api_v1/sentiment_intention_prediction", tags=["api_v1"])
async def view_a(
    auth: Depends = Depends(get_current_user),
):
    sentiment = sentiment_func()
    intention = intention_func()
    return {"sentiment": sentiment, "intention": intention}
