from enum import Enum


class PayEnum(Enum):
  Payment = 'payment'
  Return = 'return'
  Refund = 'refund'