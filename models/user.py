from datetime import datetime

from peewee import BooleanField, CharField, DateTimeField, IntegerField, Model, SqliteDatabase

database = SqliteDatabase("database.sqlite3")


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    id = IntegerField(primary_key=True)
    username = CharField(default=None, null=True)

    is_admin = BooleanField(default=False)

    created_at = DateTimeField(default=lambda: datetime.utcnow())

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    class Meta:
        table_name = "users"
