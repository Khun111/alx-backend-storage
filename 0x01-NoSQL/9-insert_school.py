#!/usr/bin/env python3
'''Module for all docs in collection'''
def insert_school(mongo_collection, **kwargs):
    '''Function for all docs in collection'''
    return mongo_collection.insert_one(kwargs).inserted_id
