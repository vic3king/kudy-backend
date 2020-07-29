import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    reference = Column(String, nullable=False)
    transaction_type = Column(Enum("withdraw", "deposit", "credit", "debit", "generic", name="ReferenceTypes"), default="generic")
    owner_id = Column(Integer,  ForeignKey("user.id"))
    owner = relationship("User", back_populates="transactions")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
