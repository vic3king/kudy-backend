from typing import Optional, Any
import datetime

from pydantic import BaseModel


# Shared properties
class InvestmentBase(BaseModel):
    name: str
    description: str
    rate: int
    lock_period: int

# Properties to receive on Investment creation
class InvestmentCreate(InvestmentBase):
    name: str
    description: str
    rate: int
    lock_period: int


# Properties to receive on Investment update
class InvestmentUpdate(InvestmentBase):
    name: Optional[str] = None
    description: Optional[str] = None
    rate: Optional[int] = None
    lock_period: Optional[int] = None


# Properties shared by models stored in DB
class InvestmentInDBBase(InvestmentBase):
    name: Optional[str] = None
    description: str
    rate: int
    lock_period: int

    class Config:
        orm_mode = True


# Properties to return to client
class Investment(InvestmentInDBBase):
    id: int
    name: str
    description: str
    rate: int
    lock_period: int


# # Properties properties stored in DB
# class InvestmentInDB(InvestmentInDBBase):
#     pass

