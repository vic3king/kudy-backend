from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Investment])
def read_investments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve investments.
    """

    investments = crud.investment.get_multi(db, skip=skip, limit=limit)
    
    return investments


@router.post("/", response_model=schemas.Investment)
def create_investment(
    *,
    db: Session = Depends(deps.get_db),
    investment_in: schemas.InvestmentCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new investment.
    """
    investment = crud.investment.get_by_name(db, name=investment_in.name)
    if investment:
        raise HTTPException(
            status_code=409,
            detail="This investment already exists in the system.",
        )

    investment = crud.investment.create(db=db, obj_in=investment_in)
    return investment


@router.patch("/{id}", response_model=schemas.Investment)
def update_investment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    investment_in: schemas.InvestmentUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an investment.
    """
    investment = crud.investment.get(db=db, id=id)

    if not investment:
        raise HTTPException(status_code=404, detail="Investment not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    investment = crud.investment.update(db=db, db_obj=investment, obj_in=investment_in)
    return investment

# @router.get("/{id}", response_model=schemas.Investment)
# def read_investment(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get investment by ID.
#     """
#     investment = crud.investment.get(db=db, id=id)
#     if not investment:
#         raise HTTPException(status_code=404, detail="Investment not found")
#     if not crud.user.is_superuser(current_user) and (investment.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return investment


# @router.delete("/{id}", response_model=schemas.Investment)
# def delete_investment(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an investment.
#     """
#     investment = crud.investment.get(db=db, id=id)
#     if not investment:
#         raise HTTPException(status_code=404, detail="Investment not found")
#     if not crud.user.is_superuser(current_user) and (investment.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     investment = crud.investment.remove(db=db, id=id)
#     return investment
