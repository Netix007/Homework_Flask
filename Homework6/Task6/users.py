from fastapi import APIRouter, HTTPException
from user_models import User, UserIn, UserUpdate
from database import users, db
from bcrypt import gensalt, hashpw

router = APIRouter()


@router.get("/users", response_model=list[User], response_model_exclude={'password'})
async def get_users(
):
    return await db.fetch_all(users.select())


@router.post("/users", response_model=User)
async def create_user(user: UserIn):
    salt = gensalt()
    password_hash = hashpw(user.password.encode("utf-8"), salt=salt)
    user.password = password_hash.decode("utf-8")
    query = users.insert().values(**user.model_dump())
    user_id = await db.execute(query=query)
    return User(**user.model_dump(), id=user_id)


@router.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    data = await db.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    query = users.update().where(users.c.id == user_id).values(**user.model_dump())
    res = await db.execute(query=query)
    if res > 0:
        return User(**user.model_dump(), id=user_id)
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    res = await db.execute(query=query)
    if res > 0:
        return {"message": "User was successfully deleted"}
    raise HTTPException(status_code=404, detail="User not found")
