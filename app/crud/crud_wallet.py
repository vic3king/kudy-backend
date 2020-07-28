from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.wallet import Wallet
from app.schemas.wallet import WalletCreate, WalletUpdate


class CRUDWallet(CRUDBase[Wallet, WalletCreate, WalletUpdate]):
    def get_by_owner_id(self, db: Session, *, owner_id: int) -> Optional[Wallet]:
        return db.query(Wallet).filter(Wallet.owner_id == owner_id).first()
        
    def create_with_owner(
        self, db: Session, *, obj_in: WalletCreate, owner_id: int
    ) -> Wallet:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


wallet = CRUDWallet(Wallet)
