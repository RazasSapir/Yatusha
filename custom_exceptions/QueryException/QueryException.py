class QueryException(Exception):
    def __init__(self, msg: str = "invalid Query"):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg