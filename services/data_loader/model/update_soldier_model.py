from rank import Rank
from typing import Optional
from pydantic import ConfigDict, BaseModel
from bson import ObjectId


class UpdateSoldierModel(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[int] = None
    rank: Optional[Rank] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": +972585979770,
                "rank": Rank.SOLDIER,
            }
        },
    )