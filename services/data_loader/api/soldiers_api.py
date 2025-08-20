from fastapi import APIRouter, status, Body

from services.data_loader.core import Database
from services.data_loader.dal_service import SoldierService
from services.data_loader.model import SoldierModel

router = APIRouter(prefix="/soldiersdb", tags=["soldiers"])
db = Database()
soldiers_service = SoldierService(db)


@router.post(
    "/",
    response_description="Add new soldier",
    response_model=SoldierModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_student(soldier: SoldierModel = Body(...)):
    return await soldiers_service.create(soldier)
