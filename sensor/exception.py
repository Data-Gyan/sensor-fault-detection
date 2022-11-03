import sys


def error_message_details(error, error_detail:sys):

    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_numer = exec_tb.tb_frame.f_code.co_firstlineno

    error_message = "Errror occured in python file [{0}] in line number [{1}] with error message {2}".format(
        file_name, line_numer, error
        )
    return error_message


'''
Class SensorException to handle customized exceptions for the current project.
    It raises raw exception alongwith error_message and error details
    which help tracing back the exceptions origin and some other related information.
'''
class SensorException(Exception):

    def __init__(self, error_message, error_detail:sys):
        """
        : error_message :  
        : error_detail : 
        """
     
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

   