from sqlalchemy.orm import Session


# model imports
from app.models.vending_machine import VendingMachine

# schema imports
from app.schemas.vending_machine.vending_machine_patch import VendingMachinePatch
from app.schemas.vending_machine.vending_machine_create import VendingMachineCreate
from app.schemas.vending_machine.vending_machine_put import VendingMachinePut

import uuid

def getVendingMachineById(
        db: Session,
        vendingMachineId: uuid.UUID
) -> VendingMachine | None:
    
    machine = db.get(VendingMachine, vendingMachineId)

    return machine

def createVendingMachine(
        db: Session,
        machineData: VendingMachineCreate
) -> VendingMachine:
    machine = VendingMachine(

        vendingMachineName=machineData.vendingMachineName,
        vendingMachineItemType=machineData.vendingMachineItemType,
        vendingMachineDescription=machineData.vendingMachineDescription,
        vendingMachineImageURL=machineData.vendingMachineImageURL,
        vendingMachineAccessType=machineData.vendingMachineAccessType
    )
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine

def putVendingMachine(
        db: Session,
        vendingMachineId: uuid.UUID,
        machineData: VendingMachinePut
) -> VendingMachine | None:
    
    machine = db.get(VendingMachine, vendingMachineId)
    
    if machine is None:
        return None

    machine.vendingMachineName = machineData.vendingMachineName
    machine.vendingMachineItemType = machineData.vendingMachineItemType
    machine.vendingMachineDescription = machineData.vendingMachineDescription
    machine.vendingMachineImageURL = machineData.vendingMachineImageURL
    machine.vendingMachineAccessType = machineData.vendingMachineAccessType

    db.commit()
    db.refresh(machine)
    return machine

def patchVendingMachine(
        db: Session,
        vendingMachineId: uuid.UUID,
        machineData: VendingMachinePatch
) -> VendingMachine | None:
    
    machine = db.get(VendingMachine, vendingMachineId)

    if machine is None:
        return None

    updateData = machineData.model_dump(exclude_unset=True)
    if "vendingMachineName" in updateData:
        machine.vendingMachineName = updateData["vendingMachineName"]
    if "vendingMachineItemType" in updateData:
        machine.vendingMachineItemType = updateData["vendingMachineItemType"]
    if "vendingMachineDescription" in updateData:
        machine.vendingMachineDescription = updateData["vendingMachineDescription"]
    if "vendingMachineImageURL" in updateData:
        machine.vendingMachineImageURL = updateData["vendingMachineImageURL"]
    if "vendingMachineAccessType" in updateData:
        machine.vendingMachineAccessType = updateData["vendingMachineAccessType"]

    db.commit()
    db.refresh(machine)
    return machine
