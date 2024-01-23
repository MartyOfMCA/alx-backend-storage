#!/usr/bin/env python3
"""
Define a function that retrieves all the database
collections in a mongodb database.
"""
import pymongo


def list_all(mongo_collection):
    """
    Retrieves a list of all documents in
    a the given database collection.

    Parameters:
        mongo_collection : Collection
        An instance of a collection from
        the pymongo.collection module.

    Returns:
        A list of documents in the given
        collection otherwise an empty
        list is returned.
    """
    return ([doc for doc in mongo_collection.find()])
