#!usr/bin/env python3
'''Module for all docs in collection'''


def list_all(mongo_collection):
    '''Function for all docs in collection'''
    return mongo_collection.find()
