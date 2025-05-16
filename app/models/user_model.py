from tortoise.models import Model
from tortoise import fields
import uuid

class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length = 10, null = False)
    username = fields.CharField(max_length = 10, null = False)
    email = fields.CharField(max_length = 20, unique = True, null = False)
    phone = fields.CharField(max_length = 15, unique = True, null = False)
    password = fields.CharField(max_length = 100, null = False)
    refresh_token = fields.CharField(max_length = 200, null = True)
    created_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

