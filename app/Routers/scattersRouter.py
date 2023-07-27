from fastapi import APIRouter
from app.Controllers.scattersController import most_important_features, least_important_features

router = APIRouter(
    prefix="/scatter"
)


@router.get("/most_important_features")
async def retrieveFeatureImportance():
    try:
        features = await most_important_features()
        return features
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/least_important_features")
def retrieveFeatureImportance():
    try:
        return least_important_features()
    except Exception as e:
        return {"error": str(e)}
    
