# MIT Pset 1: Saving with a raise

# determine how long it will take you to save enough money to make the down payment on a house


portion_down_payment = .25                                                                    # needed for down payment
current_savings = 0
r = .04                                                                                       # return on investment

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))      # from monthly salary
total_cost = float(input("Enter the cost of your dream home: "))
down_payment = portion_down_payment * total_cost
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))               # salary raise every 6 months

monthly_salary = annual_salary / 12
months = 0
while current_savings < down_payment:
    current_savings += (current_savings * r/12) + (portion_saved * monthly_salary)
    months += 1
    if not months % 6:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

print(f"Months: {months}")
