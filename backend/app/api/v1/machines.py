# imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.api.deps import getDb
from app.schemas.vending_machine.vending_machine_response import VendingMachineResponse
from app.models.vending_machine import VendingMachine

# crud imports
from app.crud.crud_vending_machine import createVendingMachine
from app.crud.crud_vending_machine import putVendingMachine
from app.crud.crud_vending_machine import patchVendingMachine
from app.crud.crud_vending_machine import getVendingMachineById

# schema imports
from app.schemas.vending_machine.vending_machine_create import VendingMachineCreate
from app.schemas.vending_machine.vending_machine_put import VendingMachinePut
from app.schemas.vending_machine.vending_machine_patch import VendingMachinePatch

import uuid



router = APIRouter(
    prefix="/machines",
    tags=["Vending Machines"]
)

@router.get("/", response_model=list[VendingMachineResponse])
def getMachine(db: Session = Depends(getDb)):
    statement = select(VendingMachine)
    machines = db.scalars(statement).all()
    return machines


@router.get("/{vendingMachineId}", response_model=VendingMachineResponse)
def getMachineById(
    vendingMachineId: uuid.UUID,
    db: Session = Depends(getDb)
):
    machine = getVendingMachineById(db, vendingMachineId)

    if machine is None:
        raise HTTPException(
            status_code=404,
                detail="Vending machine not found"
        )
    return machine

@router.post("/", response_model=VendingMachineResponse, status_code=201)
def createMachine(
    machineData: VendingMachineCreate,
    db: Session = Depends(getDb)
):
    return createVendingMachine(db, machineData)

@router.put("/{vendingMachineId}", response_model=VendingMachineResponse)
def updateMachine(
    vendingMachineId: uuid.UUID,
    machineData: VendingMachinePut,
    db: Session = Depends(getDb)
):
    machine = putVendingMachine(db, vendingMachineId, machineData)

    if machine is None:
        raise HTTPException(
            status_code=404,
              detail="Vending machine not found"
        )

    return machine

@router.patch("/{vendingMachineId}", response_model=VendingMachineResponse)
def patchMachine(
    vendingMachineId: uuid.UUID,
    machineData: VendingMachinePatch,
    db: Session = Depends(getDb)
):
    machine = patchVendingMachine(db, vendingMachineId, machineData)
    
    if machine is None:
        raise HTTPException(
            status_code=404,
              detail="Vending machine not found"
        )

    return machine
