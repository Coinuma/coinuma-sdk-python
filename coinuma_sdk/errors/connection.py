class BadRequestError(Exception):
    pass


class EndpointNotExistsError(Exception):
    pass


class TooManyRequestsError(Exception):
    pass


class InternalServerError(Exception):
    pass


class GeneralConnectionError(Exception):
    pass
