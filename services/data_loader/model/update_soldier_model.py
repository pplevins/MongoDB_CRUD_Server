from model.rank import Rank
from typing import Optional
from pydantic import ConfigDict, BaseModel
from bson import ObjectId
from pydantic_extra_types.phone_numbers import PhoneNumber


class UpdateSoldierModel(BaseModel):
    """
    A special class to represent the soldier model with optional values for update.
    Used only for updating soldier in the database, and ignoring `None` values.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[PhoneNumber] = None
    rank: Optional[Rank] = None

    # A mapping dictionary for model representation in the API
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        use_enum_values=True,
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": '+972585979770',
                "rank": Rank.SOLDIER,
            }
        },
    )
