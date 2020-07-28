from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/invest", response_model=schemas.Invest)
def create_investment(
    *,
    db: Session = Depends(deps.get_db),
    invest_in: schemas.InvestCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new user investment.
    """

    investment = crud.investment.get(db=db, id=invest_in.investment_id)

    if not investment:
        raise HTTPException(status_code=404, detail="Investment not found")

    wallet = crud.wallet.get_by_owner_id(db=db, owner_id=current_user.id)

    print(current_user.id, ">>>>>>>1>>>>>>")
    if not wallet or invest_in.amount > wallet.balance:
        raise HTTPException(
            status_code=400, detail="Low wallet balance, kindly top up."
        )

    print(wallet.balance, ">>>>>>>2>>>>>>")

    invest = crud.invest.create_with_owner(
        db=db, obj_in=invest_in, owner_id=current_user.id
    )

    wallet.balance = wallet.balance - invest_in.amount
    db.commit()
    print(wallet.balance, ">>>>>>>3>>>>>>")

    # db.refresh()
    return invest
