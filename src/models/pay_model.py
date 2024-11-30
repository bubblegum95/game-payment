import uuid
from tortoise import Model, fields
from src.type.pay_enum import PayEnum
from src.models.user_model import User

class Payment(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    customer_id = User.id
    order_id = fields.CharField(unique=True, null = False)
    type = fields.CharEnumField(enum_type=PayEnum)
    price = fields.IntField(null = False)
    receipt = fields.CharField(null = False)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "payment"
        table_description = "결제 내역 테이블"
    
    def __str__(self):
        return self.name