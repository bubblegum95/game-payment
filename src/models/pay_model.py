import uuid
from tortoise import Model, fields
from src.type.pay_enum import PayEnum

class Payment(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    type = fields.CharEnumField(enum_type=PayEnum)
    price = fields.IntField(null = False)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "payment"
        table_description = "결제 내역 테이블"
    
    def __str__(self):
        return self.name