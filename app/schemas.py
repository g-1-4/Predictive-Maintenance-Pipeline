from pydantic import BaseModel,Field

class predictionRequest(BaseModel):
    Type: str = Field(..., alias="Type")
    Air_temperature: float = Field(..., alias="Air_temperature")
    Process_temperature: float = Field(..., alias="Process_temperature")
    Rotational_speed: int = Field(..., alias="Rotational_speed")
    Torque: float = Field(..., alias="Torque")
    Tool_wear: int = Field(..., alias="Tool_wear")

    class config:
        populate_by_name = True
        extra = "ignore"