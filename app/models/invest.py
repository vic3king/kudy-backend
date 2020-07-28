import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .investment import Investment  # noqa: F401


class Invest(Base):
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    duration = Column(String, nullable=False)
    investment_id = Column(Integer, ForeignKey("investment.id"))
    owner_id = Column(Integer,  ForeignKey("user.id"))
    owner = relationship("User", back_populates="investments")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
