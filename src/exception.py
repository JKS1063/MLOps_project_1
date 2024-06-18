import sys
import logging
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() # getting the traceback info from the error details object
    file_name = exc_tb.tb_frame.f_code.co_filename # getting the file name from the traceback info object
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]" 
    # error message to be returned

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # calling the super class __init__ method
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    