from fastapi import HTTPException

from core import Database
from dal import SoldierDAL
from model import SoldierModel, SoldierCollection, UpdateSoldierModel


class SoldierService:
    def __init__(self, db: Database):
        self._dal = SoldierDAL(db)

    async def create(self, soldier: SoldierModel) -> dict:
        """Create a new Soldier dump, passing the model to Dal."""
        new_soldier = soldier.model_dump(by_alias=True, exclude=set("_id"), exclude_none=True)
        return await self._dal.create(new_soldier)

    async def list_soldiers(self) -> SoldierCollection:
        """List all Soldier instances passed from Dal."""
        soldiers = await self._dal.list()
        return SoldierCollection(soldiers=soldiers)

    async def get(self, soldier_id: str) -> dict:
        """Get a Soldier instance by ID passed from Dal."""
        soldier = await self._dal.get(soldier_id)
        if soldier is None:
            raise HTTPException(status_code=404, detail=f"Soldier {soldier_id} not found")
        return soldier

    async def update(self, soldier_id: str, soldier: UpdateSoldierModel) -> dict:
        """Update a Soldier instance by ID passed to Dal."""
        update_data = {
            k: v for k, v in soldier.model_dump(by_alias=True).items() if v is not None
        }

        # If no attribute updated, return the existing soldier
        if not update_data:
            return await self.get(soldier_id)

        updated = await self._dal.update(soldier_id, update_data)
        if updated is None:
            raise HTTPException(status_code=404, detail=f"Soldier {soldier_id} not found")
        return updated

    async def delete(self, soldier_id: str):
        """Delete a Soldier instance by ID passed to Dal."""
        deleted = await self._dal.delete(soldier_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail=f"Soldier {soldier_id} not found")
        return None
