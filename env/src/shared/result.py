from shared.error import Error


class Result:
    def __init__(self, is_success, error = Error, exception = None):
        self.is_success = is_success,
        self.error = error
        self.exception = exception
            
    def __str__(self):
        return  f'Is Success: {self.is_success} Error: {self.error} Exception: {self.exception}' 