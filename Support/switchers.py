"""
Made switcher 
"""
class SwitcherDay(object):
    def plate_to_days(self, argument):
        """Dispatch method"""
        method_name = 'plate_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid number")
        return method()
 
    def plate_0(self):
        return "4"
 
    def plate_1(self):
        return "0"
 
    def plate_2(self):
        return "0"

    def plate_3(self):
        return "1"
 
    def plate_4(self):
        return "1"
 
    def plate_5(self):
        return "2"

    def plate_6(self):
        return "2"

    def plate_7(self):
        return "3"
 
    def plate_8(self):
        return "3"
 
    def plate_9(self):
        return "4"