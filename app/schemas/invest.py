from typing import Optional, Any
import datetime
from .investment import (
    Investment,
    InvestmentCreate,
    InvestmentInDBBase,
    InvestmentUpdate,
)
from pydantic import BaseModel

# Shared properties
class InvestBase(BaseModel):
    amount: int
    duration: int
    investment_id: int
    returns: Optional[int] = 0
    potential_returns: Optional[int] = 0


# Properties to receive on Invest creation
class InvestCreate(BaseModel):
    amount: int
    duration: int
    investment_id: int


# Properties to receive on Invest update
class InvestUpdate(InvestBase):
    pass


# Properties shared by models stored in DB
class InvestInDBBase(InvestBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Invest(InvestInDBBase):
    pass


# Properties properties stored in DB
class InvestInDB(InvestInDBBase):
    pass


class InvestmentWithdraw(BaseModel):
    investment_id: int


class InvestmentShared(BaseModel):
    name: str

    class Config:
        orm_mode = True


class InvestmentHistory(InvestInDBBase):
    investment: InvestmentShared

    class Config:
        orm_mode = True

