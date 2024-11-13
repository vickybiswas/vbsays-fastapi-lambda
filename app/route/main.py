from app.route import user, task, share
from fastapi import APIRouter
from app.utils.server import settings

api_router = APIRouter()

ROUTE_BASE = settings.API_PATH
api_router.include_router(user.router, prefix="/users", tags=["Users"]) 
api_router.include_router(task.router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(share.router, prefix="/shares", tags=["Shares"])

# End of File