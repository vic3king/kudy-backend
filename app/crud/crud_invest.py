from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.invest import Invest
from app.models.investment import Investment
from app.schemas.invest import InvestCreate, InvestUpdate, InvestmentWithdraw, InvestmentHistory


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

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[InvestmentHistory]:
        return (
            db.query(self.model)
            .filter(Invest.owner_id == owner_id)
            .order_by(Invest.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_user_investment(
        self, db: Session, *, owner_id: int, investment_in: InvestmentWithdraw
    ) -> Optional[Invest]:
        return (
            db.query(Invest)
            .filter(
                Invest.owner_id == owner_id, Invest.id == investment_in.investment_id
            )
            .first()
        )


invest = CRUDInvest(Invest)
