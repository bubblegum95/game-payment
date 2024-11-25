from tortoise.models import Model
from tortoise import fields
import uuid

class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length = 10, null = False)
    username = fields.CharField(max_length = 10, null = False)
    email = fields.CharField(max_length = 20, unique = True, null = False)
    phone = fields.CharField(max_length = 11, unique = True, null = False)
    password = fields.CharField(max_length = 100, null = False)
    createdAt = fields.DateField(null = False)

class Meta:
    table = "user"
    table_description = "사용자 정보 테이블"

