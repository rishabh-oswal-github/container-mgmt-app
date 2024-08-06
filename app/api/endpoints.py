import logging
from fastapi import APIRouter, HTTPException
from app.models import Container
from app.schemas import (
    ContainerCreate,
    ContainerUpdate,
    ContainerResponse,
    FeeCalculationRequest,
    FeeCalculationResponse,
    StatisticsResponse,
)
from app.database import containers_db, fees_db
from app.utils.fee_calculator import calculate_demurrage_and_detention_fees
from datetime import date
from typing import List

router = APIRouter()

# Endpoint to create a new container
@router.post("/containers", response_model=ContainerResponse, status_code=201)
def create_container(container: ContainerCreate):
    if container.container_id in containers_db:
        raise HTTPException(status_code=400, detail="Container already exists.")
    new_container = Container(
        container_id=container.container_id,
        arrival_date=container.arrival_date,
        departure_date=container.departure_date,
    )
    containers_db[container.container_id] = new_container
    return new_container

# Endpoint to update an existing container
@router.put("/containers/{container_id}", response_model=ContainerResponse, status_code=201)
def update_container(container_id: str, container: ContainerUpdate):
    if container_id not in containers_db:
        logging.info('Creating a new Container as container does not exist')
    new_container = Container(
        container_id=container_id,
        arrival_date=container.arrival_date,
        departure_date=container.departure_date,
    )
    containers_db[container_id] = new_container
    return new_container

# Endpoint to retrieve a specific container
@router.get("/containers/{container_id}", response_model=ContainerResponse)
def get_container(container_id: str):
    container = containers_db.get(container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found.")
    return container

# Endpoint to retrieve all containers
@router.get("/containers", response_model=List[ContainerResponse])
def get_all_containers():
    return list(containers_db.values())

# Endpoint to calculate fees
@router.post("/calculate_fees", response_model=FeeCalculationResponse)
def calculate_fees(request: FeeCalculationRequest):
    try:
        container = containers_db.get(request.container_id)
        if not container:
            raise HTTPException(status_code=404, detail="Container not found.")
        
        demurrage_fee, detention_fee = calculate_demurrage_and_detention_fees(
            request.days_on_terminal, request.days_with_consignee
        )
        fee_record = FeeCalculationResponse(
            container_id=request.container_id,
            days_on_terminal=request.days_on_terminal,
            days_with_consignee=request.days_with_consignee,
            demurrage_fee=demurrage_fee,
            detention_fee=detention_fee,
            total_fee=demurrage_fee + detention_fee
        )
        fees_db[request.container_id] = fee_record
        return fee_record
    except Exception as excep_msg:
        raise excep_msg

# Endpoint to get fees for a specific container
@router.get("/fees/{container_id}", response_model=FeeCalculationResponse)
def get_fees(container_id: str):
    fee_record = fees_db.get(container_id)
    if not fee_record:
        raise HTTPException(status_code=404, detail="Fee record not found.")
    return fee_record

# Endpoint to generate statistics
@router.get("/statistics", response_model=StatisticsResponse)
def generate_statistics():
    # Clarify: Calculation of Fees is independent of containers
    # because containers don't have information about the number
    # of days container is on terminal or with consignee.
    # (or there is some relation with arrival and departure date)

    # Therefore for the statistics to work perfectly all containers
    # should have their fees calculated and saved in the fees db

    # At this point I am calculating stats based on number of containers
    # and number of fees we have in our DB. So its possible that we have
    # 5 containers 
    total_containers = len(fees_db)
    if total_containers == 0:
        return StatisticsResponse(
            total_containers=0,
            average_days_on_terminal=0.0,
            average_days_with_consignee=0.0,
            total_demurrage_fee=0.0,
            total_detention_fee=0.0,
            average_demurrage_fee_per_container=0.0,
            average_detention_fee_per_container=0.0
        )
    
    total_days_on_terminal = sum(fee.days_on_terminal for fee in fees_db.values())
    total_days_with_consignee = sum(fee.days_with_consignee for fee in fees_db.values())
    total_demurrage_fee = sum(fee.demurrage_fee for fee in fees_db.values())
    total_detention_fee = sum(fee.detention_fee for fee in fees_db.values())

    return StatisticsResponse(
        total_containers=total_containers,
        average_days_on_terminal=total_days_on_terminal / total_containers,
        average_days_with_consignee=total_days_with_consignee / total_containers,
        total_demurrage_fee=total_demurrage_fee,
        total_detention_fee=total_detention_fee,
        average_demurrage_fee_per_container=total_demurrage_fee / total_containers,
        average_detention_fee_per_container=total_detention_fee / total_containers
    )
