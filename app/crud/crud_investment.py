from typing import List,Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.investment import Investment
from app.schemas.investment import InvestmentCreate, InvestmentUpdate


class CRUDInvestment(CRUDBase[Investment, InvestmentCreate, InvestmentUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Investment]:
        return db.query(Investment).filter(Investment.name == name).first()

    def create_with_owner(
        self, db: Session, *, obj_in: InvestmentCreate, owner_id: int
    ) -> Investment:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Investment]:
        return (
            db.query(self.model)
            .filter(Investment.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


investment = CRUDInvestment(Investment)
