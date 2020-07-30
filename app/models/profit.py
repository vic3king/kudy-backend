import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .invest import Invest  # noqa: F401

class Profit(Base):
    id = Column(Integer, primary_key=True, index=True)
    invest_id = Column(Integer, ForeignKey("invest.id"))
    returns = Column(Integer, default=0, nullable=True)
    investment = relationship("Invest", back_populates="investment")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
