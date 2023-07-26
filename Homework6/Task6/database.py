from sqlalchemy import MetaData, create_engine, Table, Column, String, Integer, Numeric, ForeignKey, Date, Boolean
from databases import Database
from settings import settings

db = Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(settings.NAME_MAX_LENGTH)),
    Column("last_name", String(settings.NAME_MAX_LENGTH)),
    Column("email", String(settings.EMAIL_MAX_LENGTH)),
    Column("password", String(settings.PASSWORD_MAX_LENGTH)),
)

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(settings.NAME_MAX_LENGTH)),
    Column("description", String(settings.NAME_MAX_LENGTH)),
    Column("cost", Numeric(10, 2)),
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False),
    Column("item_id", Integer, ForeignKey("items.id", ondelete='CASCADE'), nullable=False),
    Column("order_date", Date()),
    Column("is_done", Boolean),
)

metadata.create_all(engine)
