#!/usr/bin/env python3
"""
Define a function that adds a new document
to a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a MongoDB collection.

    Parameters:
        mongo_collection : Collection
        An instance of a collection from
        the pymongo.collection module.

        kwargs : dictionary
        Key-value pairs containing values for
        the new document.

    Returns:
        The id for the new document created.
    """
    return (mongo_collection.insert_one(kwargs).inserted_id)
