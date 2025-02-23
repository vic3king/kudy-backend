import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Wallet(Base):
    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer, nullable=False)
    owner_id = Column(Integer,  ForeignKey("user.id"))
    owner = relationship("User", back_populates="wallet")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
