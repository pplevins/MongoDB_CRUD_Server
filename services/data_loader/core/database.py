import os

import pymongo
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi


# TODO: Add documentation
class Database:
    _db = None
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            mongodb_url = os.environ["MONGODB_URL"]
            _client = AsyncMongoClient(
                mongodb_url,
                server_api=pymongo.server_api.ServerApi(version="1", strict=True, deprecation_errors=True))
            cls._db = cls._client.soldiersdb
        return cls._client

    @classmethod
    def get_soldiers_collection(cls):
        if cls._db is None:
            cls.get_client()
        return cls._db.get_collection("soldiers")
