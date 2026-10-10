from .vending_machine_base import BaseModel

class VendingMachinePatch(BaseModel):
    vendingMachineName: str | None = None
    vendingMachineItemType: str | None = None
    vendingMachineDescription: str | None = None
    vendingMachineImageURL: str | None = None
    vendingMachineAccessType: str | None = None