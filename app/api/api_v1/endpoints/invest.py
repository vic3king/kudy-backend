from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/history")
def read_investments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users investments.
    """

    investments = crud.invest.get_multi_by_owner(
        db=db, owner_id=current_user.id, skip=skip, limit=limit
    )

    return investments


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

    if not wallet or invest_in.amount > wallet.balance:
        raise HTTPException(
            status_code=400, detail="Low wallet balance, kindly top up."
        )

    profit = invest_in.amount * (investment.rate / 100)
    potential_return = invest_in.amount + profit
    invest_in.potential_returns = potential_return
    invest = crud.invest.create_with_owner(
        db=db, obj_in=invest_in, owner_id=current_user.id
    )

    wallet.balance = wallet.balance - invest_in.amount
    db.commit()

    crud.transaction.create_with_owner(
        db=db,
        obj_in={
            "amount": invest_in.amount,
            "reference": f"wallet debit for investment in {investment.name}",
            "transaction_type": "debit",
        },
        owner_id=current_user.id,
    )

    return invest


@router.post("/withdraw", response_model=schemas.Wallet)
def investment_withdraw(
    *,
    db: Session = Depends(deps.get_db),
    investment_in: schemas.InvestmentWithdraw,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Withdraw from investment.
    """

    wallet = crud.wallet.get_by_owner_id(db=db, owner_id=current_user.id)


    investment = crud.invest.get_user_investment(
        db=db, investment_in=investment_in, owner_id=current_user.id
    )

    if not investment:
        raise HTTPException(status_code=404, detail="Investment not found")

    if wallet and investment.returns > 0:
        wallet.balance += investment.returns

        crud.transaction.create_with_owner(
            db=db,
            obj_in={
                "amount": investment.returns,
                "reference": "investment withdrawal to wallet",
                "transaction_type": "credit",
            },
            owner_id=current_user.id,
        )

        investment.returns = 0
        db.commit()

        return wallet

    raise HTTPException(
        status_code=404,
        detail="Investment is not matured and thus there is no funds available for withdrawal",
    )
