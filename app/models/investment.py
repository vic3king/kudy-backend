import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Investment(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False,index=True)
    rate = Column(Integer,nullable=False,default=14, index=True)
    lock_period = Column(Integer, nullable=False,default=14, index=True)
    investor = relationship("Invest", back_populates="investment")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
