from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/me", response_model=schemas.Wallet)
def read_wallet(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get wallet by User ID.
    """
    wallet = crud.wallet.get_by_owner_id(db=db, owner_id=current_user.id)

    if not wallet:
        wallet_in = {"balance": 0}
        wallet = crud.wallet.create_with_owner(
            db=db, obj_in=wallet_in, owner_id=current_user.id
        )
        return wallet

    return wallet


@router.post("/top-up", response_model=schemas.Wallet)
def wallet_top_up(
    *,
    db: Session = Depends(deps.get_db),
    wallet_in: schemas.WalletCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Top up wallet.
    """
    wallet = crud.wallet.get_by_owner_id(db=db, owner_id=current_user.id)

    if wallet:
        wallet.balance += wallet_in.amount
        db.commit()
        return wallet

    if not wallet:
        del wallet_in.owner_id
        del wallet_in.amount
        wallet_in.balance = 0
        wallet = crud.wallet.create_with_owner(
            db=db, obj_in=wallet_in, owner_id=current_user.id
        )
        return wallet

