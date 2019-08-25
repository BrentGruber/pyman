"""collection.py

Contains Class definititions with ability to convert Postman collection schema into python objects

"""
import related

@related.immutable
class Info(object):
    """Info class contains top level postman collection info"""
    
    postman_id = related.StringField(key="_postman_id")
    name = related.StringField(required=True)
    schema = related.URLField()

@related.immutable
class Header(object):
    """Header class contains representation of a request headers"""
    
    key = related.StringField()
    value = related.StringField()

@related.immutable
class URL(object):
    """URL class contains the postman representation of an API url"""
    
    raw = related.URLField()
    protocol = related.StringField()
    host = related.SequenceField(str)
    path = related.SequenceField(str)

@related.immutable
class Request(object):
    """Request class contains HTTP request info for an API request"""
    
    method = related.StringField()
    header = related.SequenceField(Header)
    url = related.ChildField(URL)

@related.immutable
class Item(object):
    """Item class contains information for postman requests within a collection"""
    
    name = related.StringField()
    request = related.ChildField(Request)
    #TODO: from Postman 2.1 schema: https://schema.getpostman.com/json/collection/latest/docs/index.html
    #response = related.SequenceField(Response)
    #event = related.SequenceField(Event)
    #variable = related.SequenceField(Variable)
    #auth = related.ChildField(Auth)

@related.immutable
class Collection(object):
    """Collection class is a representation of postman collections stored within a python object."""

    info = related.ChildField(Info)
    item = related.SequenceField(Item,"item")
