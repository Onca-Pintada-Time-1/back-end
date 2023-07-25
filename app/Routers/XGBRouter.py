from fastapi import APIRouter
from app.Controllers import XGBController as XGB

router = APIRouter(
    prefix="/XGB"
)


@router.get("/data")
async def retrieveFeatureImportance():
    try:
        return await XGB.retrieveData()
    except Exception as e:
        return {"error": str(e)}
