"""collection.py

contains class definition for Collection objects and nested Request objects.
collection - represents an entire Postman collection
request - represents an individual request within a Postman collection

"""

class Collection:
    """Collection class is a representation of postman collections stored within a python object."""

    def __init__(self, name, base_url, auth, requests):
        """
        Collection constructor, builds Collection object from input data

        '''
        Attributes
        ---------- 
            name: str
                name of collection   
            base_url: str
                url consistent with each request within collection
            auth: tuple|str  
                authorization used for api calls
            requests: list(Request)
                list of request objects within the collection

        Methods
        -------
            definition()
                returns a string representing a python class definition for 
        """

        self.base_url = base_url
        self.auth = auth
        self.requests = requests

