#!/usr/bin/env python3
"""
Define a function that updates items of a
document based on a criteria.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topic fields of a document in the
    given MongoDB collection matching the given
    name.

    Parameters:
        mongo_collection : Colelction
        An instance of a collection from
        the pymongo.collection module.

        name : string
        The name of the school to update.

        topics : list
        A list of strings containing list of
        topics treated in the school.
    """
    schools = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
