#import
from app.database.base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime

import uuid
from datetime import datetime, timezone


class VendingMachine(Base):
    __tablename__ = "vending_machines"
    vendingMachineId: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    vendingMachineName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # This describes the items held in the machine
    vendingMachineItemType: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    # this describes the machine it self theme or what player can expect of the machine
    vendingMachineDescription: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    vendingMachineImageURL: Mapped[str | None] = mapped_column(
        String(),
        nullable=True
    )

    vendingMachineIsActive: Mapped[bool] = mapped_column(
        nullable=False,
        default=True
    )

    vendingMachineIsDefault: Mapped[bool] = mapped_column(
        nullable=False,
        default=False
    )

    vendingMachineCreatedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    vendingMachineAccessType: Mapped[str] = mapped_column(
        String(),
        nullable=False
     )
