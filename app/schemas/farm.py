from pydantic import BaseModel, Field, ConfigDict

class FarmCreate(BaseModel):
    owner_id: str
    name: str = Field(min_length=2, max_length=120)
    city: str
    price_per_night: float = Field(gt=0)
    capacity: int = Field(gt=0)

class FarmOut(FarmCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    is_active: bool