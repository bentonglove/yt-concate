import logging


# https://docs.python.org/3/library/logging.html
# Loggers have the following attributes and methods. Note that Loggers should NEVER be instantiated directly,
# but always through the module-level function logging.getLogger(name).
# Multiple calls to getLogger() with the same name will always return a reference to the same Logger object.
# init a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatters specify the layout of log records in the final output.
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')

# Handlers send the log records (created by loggers) to the appropriate destination.
# send to a file~
file_handler = logging.FileHandler("test.log")
# config the attribute to a handler
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
# add handler into a list
logger.addHandler(file_handler)

# another handler to send logs to a screen
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)



