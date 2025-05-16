import uuid
from tortoise import Model, fields
from app.type.pay_enum import PayEnum

class Payment(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    customer_id = fields.ForeignKeyField("models.User", related_name="payments")
    order_id = fields.CharField(unique=True, null=False, max_length=20)
    type = fields.CharEnumField(enum_type=PayEnum)
    price = fields.IntField(null=False)
    receipt = fields.CharField(null=False, max_length=30)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "payment"
        table_description = "결제 내역 테이블"
    
    def __str__(self):
        return self.name