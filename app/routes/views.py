from __future__ import annotations

from fastapi import APIRouter, Depends

from app.apis.api_v1.prediction import prediction as prediction
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of TEB Project FastAPI. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.get("/api_v1/sentiment_intention_prediction", tags=["api_v1"])
async def sentiment_intention_prediction(
    auth: Depends = Depends(get_current_user),
):
    # Define error. This is a list of errors that will be returned to the user.
    errors = []

    sentiments, intentions = prediction(errors)

    return {"sentiments": sentiments, "intentions": intentions, "errors": errors}
