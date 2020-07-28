from typing import Optional

from pydantic import BaseModel


# Shared properties
class WalletBase(BaseModel):
    owner_id: Optional[int] = None
    balance: Optional[int] = None


# Properties to receive on Wallet creation
class WalletCreate(WalletBase):
    amount: int


# Properties to receive on Wallet update
class WalletUpdate(WalletBase):
    pass


# Properties shared by models stored in DB
class WalletInDBBase(WalletBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Wallet(WalletInDBBase):
    pass


# Properties properties stored in DB
class WalletInDB(WalletInDBBase):
    pass
