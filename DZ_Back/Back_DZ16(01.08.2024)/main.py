if __name__ == "__main__": 
    from database import newEmployee
    from database import getEmployeeId
    from database import fireEmployee
    from database import getEmployeeRecord
    from database import getFiredEmployees
    from database import getSalaryStats
    
    new_employee_result = newEmployee("Dwight Shrute", "1987-12-11", "Salesman", 5000)
    print(new_employee_result)

    new_employee_result1 = newEmployee("Jim Halpert", "1987-05-04", "Salesman", 5000)
    print(new_employee_result1)

    new_employee_result2 = newEmployee("Oscar Menendes", "1985-10-06", "Accountant", 7000)
    print(new_employee_result2)

    new_employee_result3 = newEmployee("Pam Beesely", "1989-07-07", "Receptionist", 4000)
    print(new_employee_result3)

    new_employee_result4 = newEmployee("Ryan Wednesday", "1993-01-01", "Temp", 1000)
    print(new_employee_result4)

    new_employee_result5 = newEmployee("Angela Bauer", "1988-01-01", "Accountant", 7000)
    print(new_employee_result5)

    fire_employee_result = fireEmployee(1)
    print(fire_employee_result)

    get_employee_id_result = getEmployeeId("Dwight")
    print(get_employee_id_result)

    get_employee_record_result = getEmployeeRecord(1)
    print(get_employee_record_result)

    fired_employees = getFiredEmployees()
    print("Fired employee:")
    for employee in fired_employees:
        print(f"{employee['id']} - {employee['firstName']} {employee['lastName']}")

    salary_stats = getSalaryStats()
    print("\nSalary stats:")
    print(f"Total salary: {salary_stats['totalSalary']}")
    print(f"Min salary: {salary_stats['minSalary']}")
    print(f"Max salary: {salary_stats['maxSalary']}")
    print(f"Average salary: {salary_stats['avgSalary']}")
    print(f"Median salary: {salary_stats['medianSalary']}")