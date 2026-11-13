from sqlalchemy import String, Integer, Numeric, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class Farm(Base):
    __tablename__ = "farms"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[str] = mapped_column(String(64), index=True)
    name: Mapped[str] = mapped_column(String(120))
    city: Mapped[str] = mapped_column(String(80), index=True)
    price_per_night: Mapped[float] = mapped_column(Numeric(10, 2))
    capacity: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[str] = mapped_column(DateTime, server_default=func.now())