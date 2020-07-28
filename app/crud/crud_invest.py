from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.invest import Invest
from app.schemas.investment import InvestCreate, InvestUpdate


class CRUDInvest(CRUDBase[Invest, InvestCreate, InvestUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: InvestCreate, owner_id: int
    ) -> Invest:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


invest = CRUDInvest(Invest)
