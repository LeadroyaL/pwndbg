PAGE_SIZE = 0x1000
PAGE_MASK = ~(PAGE_SIZE - 1)
MMAP_MIN_ADDR = 0x8000


class DbgException(Exception):
    pass


class DbgMemoryException(DbgException):
    pass
