from enum import Enum


class Error(Enum):
    NONE = 1,
    IN_DATABASE_CONNECTION = 2,
    GET_DATA= 3,
    INSERT_DATA = 4