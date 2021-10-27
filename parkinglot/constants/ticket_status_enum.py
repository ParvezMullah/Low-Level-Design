from enum import Enum


class TicketStatusEnum(Enum):
    pending = 0
    paid = 1
    lost = 2
    cancelled = 3
