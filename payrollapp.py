import payroll
import employees
import employeemanagement

manager = employees.Manager(101, 'Sekhar', 5000)
developer = employees.Developer(102, 'Srinivasan', 2500)
salesman = employees.Salesman(103, "Sri", 1000, 1500)
worker = employees.Worker(104, "Lucky", 10, 250)
consultant = employees.Consultant(105, "Raj", 60, 5)

employees = [manager, developer, salesman, worker, consultant]

ems = employeemanagement.PerformanceManager()
ems.track(employees, 40)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll(employees)