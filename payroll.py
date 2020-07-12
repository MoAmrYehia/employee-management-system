import datetime
import calendar


class PayrollManagementSystem:
    
    def calculate_payroll(self, employees):
        print("Payroll Management System")
        print("=========================")
        
        for employee in employees:
            print(f"Employee #:{employee.id}\nEmployee Name :{employee.name}")
            print(f"Amount :{employee.calculate_payroll()}")  
            print("----------------------------------------")
            
class PartTimePolicy:
    def __init__(self, total_hours, rate_per_hour):
        self.total_hours = total_hours
        self.rate_per_hour = rate_per_hour

    def calculate_payroll(self):
        return self.total_hours * self.rate_per_hour
    
class SalaryPolicy:
    def __init__(self, rate_per_day):
        self.rate_per_day = rate_per_day
        
    def calculate_payroll(self):
        today = datetime.datetime.now()
        totalDays = calendar.monthrange(today.year, today.month)[1]
        return self.rate_per_day * totalDays
    
class CommissionPolicy(SalaryPolicy):    
    def __init__(self, rate_per_day, commission):
        super().__init__(rate_per_day)
        self.commission = commission

    def calculate_payroll(self):
        salary = super().calculate_payroll()
        return salary + self.commission