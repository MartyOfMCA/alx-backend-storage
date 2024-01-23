#!/usr/bin/env python3
"""
Define a function to fetch a list of documents
having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Fetch documents containing the given
    topic.

    Parameters:
        mongo_colelction : Collection
        An instance of a collection from
        the pymongo.collection module.

        topic : string
        The search topic used as the criteria.

    Returns:
        A list of schools matching the given
        criteria.
    """
    return (school for school in mongo_collection.find({"topics": topic}))
