#!/usr/bin/env python3
"""
Define a function returning student records
sorted on a field.
"""


def top_students(mongo_collection):
    """
    Returns the top students sorted by their
    average score.

    Parameters:
        mongo_collection : Collection
        An instance of a colelction from
        the pymongo.collection module.

    Returns:
        A cursor object containing student
        documents ordered by averge score
        field.
    """
    return (mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}}},
        {"$project": {"_id": 1, "name": 1, "averageScore": 1}},
        {"$sort": {"averageScore": -1}}
    ]))
