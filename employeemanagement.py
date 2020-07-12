class PerformanceManager:
    def track(self, employees, hours):
        print("Tracking Employee Performance")
        print("=============================")
        for employee in employees:
            stuts = employee.work(hours)  
            print (f"{employee.name} : {stuts}")
            print("----------------------------------------")
            
class ManagerRoll:
    def work(self, hours):
        return f"Manager is handling the project team for {hours} hours"

class DeveloperRoll:
    def work(self, hours):
        return f"Developer is working on the project team for {hours} hours"

class SalesRoll:
    def work(self, hours):
        return f"Salesman is handling the client call for {hours} hours"

class WorkerRoll:
    def work(self, hours):
        return f"worker has completed his task in {hours} hours"