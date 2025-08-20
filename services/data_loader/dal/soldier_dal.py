from bson import ObjectId
from pymongo import ReturnDocument

from core import Database


class SoldierDAL:
    """Class to represent soldier's Data Layer, and implementing CRUD operations for soldier."""

    def __init__(self, db: Database):
        """Constructor."""
        self.collection = db.get_soldiers_collection()

    async def create(self, soldier: dict) -> dict:
        """Create a new soldier record in the database."""
        result = await self.collection.insert_one(soldier)
        soldier["id"] = result.inserted_id
        return soldier

    async def list(self, limit: int = 1000) -> list:
        """List all soldiers in the database."""
        return await self.collection.find().to_list(limit)

    async def get(self, soldier_id: str) -> dict | None:
        """Get a soldier by its ID, return None if it doesn't exist."""
        return await self.collection.find_one({"_id": ObjectId(soldier_id)})

    async def delete(self, student_id: str) -> int:
        """Delete a soldier by its ID, return 0 if it doesn't exist."""
        result = await self.collection.delete_one({"_id": ObjectId(student_id)})
        return result.deleted_count

    async def update(self, student_id: str, update_data: dict) -> dict | None:
        """Update a soldier record in the database, return None if it doesn't exist."""
        return await self.collection.find_one_and_update(
            {"_id": ObjectId(student_id)},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER,
        )
