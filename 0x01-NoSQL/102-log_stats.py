#!/usr/bin/env python3
"""
Define a function that prints stats from
a log stored in MongoDB.
"""
from pymongo import MongoClient


def documents_count(collection, q_key=None, q_val=None):
    """
    Counts the number of documents matching
    the given method. Prints top 10 IPs
    in collection.

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


def print_top_ips(collection, limit):
    """
    Prints the top IPs found in the
    given collection.

    Parameters:
        collection : Collection
        An instance of a colelction from
        the pymongo.collection module.

        limit : int
        The total number of records
        to retrieve.
    """
    print("IPs:")
    [print(f"\t{item.get('_id')}: {item.get('count')}")
        for item in collection.aggregate([
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": limit}
            ])]


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
    print_top_ips(nginx_coll, 10)
