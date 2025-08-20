from fastapi import APIRouter, status, Body
from fastapi.responses import Response

from core import Database
from dal_service import SoldierService
from model import SoldierModel, UpdateSoldierModel

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
async def create_soldier(soldier: SoldierModel = Body(...)):
    return await soldiers_service.create(soldier)


@router.get(
    "/",
    response_description="List all soldiers",
)
async def get_all():
    return await soldiers_service.list_soldiers()


@router.get(
    "/{soldier_id}",
    response_description="Get a single soldier",
    response_model=SoldierModel,
    response_model_by_alias=False,
)
async def get_soldier(soldier_id: str):
    return await soldiers_service.get(soldier_id)


@router.put(
    "/{id}",
    response_description="Update a soldier",
    response_model=SoldierModel,
    response_model_by_alias=False,
)
async def update_soldier(soldier_id: str, soldier: UpdateSoldierModel = Body(...)):
    return await soldiers_service.update(soldier_id, soldier)


@router.delete(
    "/{id}",
    response_description="Delete a soldier",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_soldier(soldier_id: str):
    await soldiers_service.delete(soldier_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
