from enum import Enum

MAX_ISSUE_BOOKS = 5
MAX_BOOK_HOLDING_DAYS = 10


class PaymentStatusEnum(Enum):
    initiated = 0
    cancelled = 1
    failed = 2
    paid = 3


class BookFormatEnum(Enum):
    news_paper = 0
    hardcopy = 1
    softcopy = 2
    journal = 3


class BookTypeEnum(Enum):
    scifi = 0
    adventure = 1
    romantic = 2

