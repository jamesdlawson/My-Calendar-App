
from contextlib import contextmanager
import logging

from pymongo import MongoClient


@contextmanager
def mongo_collection(collection: str = None):
    conn = MongoClient('mongodb://localhost:27017/')
    logging.warn('connected to DB')
    collection = conn.local[collection]
    yield collection
    conn.close()
    logging.warn('closed connection to DB')