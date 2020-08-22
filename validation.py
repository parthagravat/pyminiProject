import re

class validation:

    def validatemob(self , mob):
        pattern = re.compile(r'\d{10}')
        if(pattern.match(mob)):
            return True
        else:
            print("Re-enter Mobile Number")
            return False

    def validateemail(self , email):
        pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
        if(pattern.match(email)):
            return True
        else:
            return False