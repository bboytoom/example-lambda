from config.mongo_db import mongo_db


class User:

    def search_user():
        db = mongo_db('TestDatabase')
        connect = db['users']

        return connect.find_one({})
