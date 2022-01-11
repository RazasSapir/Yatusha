class QueryException(Exception):

    def __init__(self, msg="Invalid Query"):
        self.message = msg

    def __str__(self):
        return self.message
