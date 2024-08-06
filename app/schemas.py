from pydantic import BaseModel, Field
from datetime import date

class ContainerCreate(BaseModel):
    container_id: str = Field(..., json_schema_extra={"examples": ["CONT1"]})
    arrival_date: date = Field(..., json_schema_extra={"examples": ["2023-06-01"]})
    departure_date: date = Field(..., json_schema_extra={"examples": ["2023-06-10"]})

class ContainerUpdate(BaseModel):
    arrival_date: date = Field(..., json_schema_extra={"examples": ["2023-06-01"]})
    departure_date: date = Field(..., json_schema_extra={"examples": ["2023-06-20"]})

class ContainerResponse(BaseModel):
    container_id: str
    arrival_date: date
    departure_date: date
    status: str

class FeeCalculationRequest(BaseModel):
    container_id: str = Field(..., json_schema_extra={"examples": ["CONT1"]})
    days_on_terminal: int = Field(..., json_schema_extra={"examples": [10]})
    days_with_consignee: int = Field(..., json_schema_extra={"examples": [12]})

class FeeCalculationResponse(BaseModel):
    container_id: str
    days_on_terminal: int
    days_with_consignee: int
    demurrage_fee: float
    detention_fee: float
    total_fee: float

class StatisticsResponse(BaseModel):
    total_containers: int
    average_days_on_terminal: float
    average_days_with_consignee: float
    total_demurrage_fee: float
    total_detention_fee: float
    average_demurrage_fee_per_container: float
    average_detention_fee_per_container: float
