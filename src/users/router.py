from fastapi import APIRouter

router = APIRouter(tags=["Users 👥"], prefix="/users")


@router.get("/")
async def get_users():
    return {"users": "Some data"}
