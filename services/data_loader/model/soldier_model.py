from model.rank import Rank
from typing import Optional
from pydantic import ConfigDict, BaseModel, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

# Represents an ObjectId field in the MongoDB database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class SoldierModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone_number: PhoneNumber = Field(...)
    rank: Rank = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        use_enum_values=True,
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "+972585979770",
                "rank": Rank.SOLDIER,
            }
        },
    )
