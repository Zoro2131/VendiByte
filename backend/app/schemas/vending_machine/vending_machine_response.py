# imports 
from uuid import UUID
from datetime import datetime
from pydantic import ConfigDict

# import base machine
from .vending_machine_base import VendingMachineBase


# Data returned to the Andriod App
class VendingMachineResponse(VendingMachineBase):
    vendingMachineId: UUID
    vendingMachineIsActive: bool = True
    vendingMachineIsDefault: bool = True
    vendingMachineAccessType: str
    vendingMachineCreatedAt: datetime

    model_config = ConfigDict(from_attributes=True)