
'''
Create exceptions based on your inputs. Please follow the tasks below.

 - Capture and handle system exceptions
 - Create custom user-based exceptions
'''


class CustomInputError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
