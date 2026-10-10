# imports 
from .vending_machine_base import VendingMachineBase

# Data needed when creating a new vending machine 
class VendingMachineCreate(VendingMachineBase):
    VendingMachineAccessType: str
