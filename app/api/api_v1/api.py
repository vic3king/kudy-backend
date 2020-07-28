from fastapi import APIRouter

from app.api.api_v1.endpoints import investments, login, users, utils, invest, wallet

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(investments.router, prefix="/investments", tags=["investments"])
api_router.include_router(invest.router, prefix="/investments", tags=["invest"])
api_router.include_router(wallet.router, prefix="/wallet", tags=["wallet"])