
#class Employee

class Employee:
    def __init__(self , employeeId , employeeName , role , ageInrole):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.role = role
        self.ageInrole = ageInrole


class Organisation:
    #def __init__(self , employeeList):
     #   self.employeeList = employeeList
    
    employeeList = [] , status_dict = {}
    def findPromotionEligibilityStatus(self , noOfYears):
        if(noOfYears=0):
            employeeList.add('eligible')
        
        elif(noOfYears>0):
            employeeList.add('overdue')

            
