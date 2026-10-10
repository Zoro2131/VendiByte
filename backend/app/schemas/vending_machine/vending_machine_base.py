#imports 
from pydantic import BaseModel

# Base apptrubites for a vending machine
class VendingMachineBase(BaseModel):
    vendingMachineName: str
    vendingMachineItemType: str
    vendingMachineDescription: str | None = None
    vendingMachineImageURL: str | None = None

