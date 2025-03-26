from enum import Enum


class OrderStatus(Enum):
    PENDING = "ожидается"
    PROCESSING = "в обработке"
    SHIPPED = "отправлен"
    DELIVERED = "доставлен"
    CANCELLED = "отменен"
    RETURNED = "возвращен"
    FAILED = "ошибка"
    ON_HOLD = "на удержании"
