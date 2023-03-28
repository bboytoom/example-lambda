import os
import certifi
import logging

from pymongo import MongoClient


ca = certifi.where()
logger = logging.getLogger(__name__)
client = MongoClient(os.environ.get('MONGODB_URL'), tlsCAFile=ca)


def mongo_db(database):
    try:
        db_connection = client[database]
    except ConnectionError as e:
        logger.error(e)

        return None

    return db_connection
