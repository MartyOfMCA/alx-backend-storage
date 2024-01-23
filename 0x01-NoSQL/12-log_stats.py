#!/usr/bin/env python3
"""
Define a function that prints stats from
a log stored in MongoDB.
"""
from pymongo import MongoClient


def documents_count(collection, q_key=None, q_val=None):
    """
    Counts the number of documents matching
    the given method.

    Parameters:
        colelction : Collection
        An instance of a collection from
        the pymongo.collection module.

        q_key : string, optional
        The key used to apply the filter
        when querying the collection.
        No filters are applied if it's
        None.

        q_val : string, optional
        The value used to apply the filter
        when querying the collection. This
        value maps with the given key.
        No filters are applied if it's None.

    Returns:
        The number of documents (equivalent
        to log count) matching the given
        criteria.
    """
    return (collection.count_documents({} if q_key is None and q_val is None
            else {q_key: q_val}))


if (__name__ == "__main__"):
    conn_str = MongoClient("mongodb://127.0.0.1:27017")
    db = conn_str.logs
    nginx_coll = db.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{documents_count(nginx_coll)} logs")
    print("Methods:")
    [print(f"\tmethod {method}: \
{documents_count(nginx_coll, 'method', method)}")
        for method in methods]
    print(f"{documents_count(nginx_coll, 'path', '/status')} status check")
