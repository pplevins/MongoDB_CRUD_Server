from rank import Rank
from typing import Optional, List
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class SoldierModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone_number: int = Field(...)
    rank: Rank = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": +972585979770,
                "rank": Rank.SOLDIER,
            }
        },
    )
