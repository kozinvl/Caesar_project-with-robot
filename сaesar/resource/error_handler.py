import functools
import logging


def create_logger():
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger("inner logger")
    logger.setLevel(logging.INFO)
    return logger


def logger_exception(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)
        except Exception:
            # log the exception
            err = "There was an exception in  "
            err += function.__name__
            logger.exception(err)

            # re-raise the exception
            raise

    return wrapper
