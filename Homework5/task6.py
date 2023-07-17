from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr, Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="FastAPI App")
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class UserDump(BaseModel):
    name: str
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(..., min_length=8, regex=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).*$",
                          description="Password of the user")


users = [
    User(
        id=1,
        name="Sergey",
        email="aaaa@ya.ru",
        password="jfsSSdfjksdlfj11!"
    )
]


@app.get("/users", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("all_users.html", {"request": request, "name": "All users", "users": users})


@app.get("/add_user_form", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request, "name": "Add user"})


@app.post("/add_user")
async def add_user(request: Request):
    da = await request.form()
    da = jsonable_encoder(da)
    print(type(da))
    new_id = 1
    if users:
        new_id = max(users, key=lambda x: x.id).id + 1
    try:
        new_user = UserDump(name=da["name"], email=da["email"], password=da["password"])
        users.append(
            User(
                id=new_id,
                name=new_user.name,
                email=new_user.email,
                password=new_user.password
            )
        )
        return "User add"
    except ValueError:
        return "Please, Input correct data"
