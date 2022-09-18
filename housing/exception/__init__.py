import os
iport sys

class HousingException(Exception):   #using exception class from parent and creating our own housingexception class
    pass

    def __init__(self, error_message: Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message = HousingException.get_detailed_error_message(error_message= error_message, 
                                                                                        error_detail= error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """

        _,_ ,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script: [{file_name}] error message: [{error_message}] 
        return error_message


   Amazing! Now again this course is going to be a Boom as earlier one because this FSDS course will not only help techies but also 
   going to help non tech people to get into the Data Science Industry. Well, Hats off to Sudhnashu sir, krish Sir and entire iNeuron technical consultant team.