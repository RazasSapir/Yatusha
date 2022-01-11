class QueryException(Exception):
    __msg = ""

    def __init__(self, msg=""):
        self.__msg = msg

    def __str__(self):
        return f"{self.__msg}"
