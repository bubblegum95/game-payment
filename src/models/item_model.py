import uuid
from tortoise import Model, fields

class Item(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length = 10, null = False)
    description = fields.CharField(max_length = 100, null = False)
    amount = fields.IntField(null = False)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "item"
        table_description = "상품 테이블"

    def __str__(self):
        return self.name