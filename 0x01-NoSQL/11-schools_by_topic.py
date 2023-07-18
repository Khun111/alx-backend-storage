#!usr/bin/env python3
'''Module for all docs with specific topic'''
def schools_by_topic(mongo_collection, topic):
    '''Function for all docs with specific topic'''
    return mongo_collection.find({"topics": topic})
