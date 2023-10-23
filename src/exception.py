# Import the sys module for system-level operations
import sys

# Import the logging module from a custom source (src.logger)
from src.logger import logging


# Define a function called error_message_detail that takes an error object and sys details
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()  # Get information about the exception
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the name of the file where the exception occurred
    error_message = 'Error occurred in python script name [{0}] line number [{1}] error message[{2}]'.format(
       file_name, exc_tb.tb_lineno, str(error))  # Format an error message

    return error_message  # Return the error message

# Define a custom exception class that inherits from the built-in Exception class
class CustomException(Exception):
    # Define the constructor for this class, which takes an error message and sys details
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # Call the constructor of the parent class
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Get detailed error message

    # Define a string representation for the exception
    def __str__(self):
        return self.error_message  # Return the detailed error message
