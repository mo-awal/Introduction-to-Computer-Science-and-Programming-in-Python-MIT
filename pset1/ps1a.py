# Part A: House Hunting
# determine how long it will take you to save enough money to make the down payment on a house

"""
1. Call the cost of your dream home total_cost.
2. Call the portion of the cost needed for a down payment portion_down_payment. For
simplicity, assume that portion_down_payment = 0.25 (25%).
3. Call the amount that you have saved thus far current_savings. You start with a current
savings of $0. 
4. Assume that you invest your current savings wisely, with an annual return of r (in other words,
at the end of each month, you receive an additional current_savings*r/12 funds to put into
your savings - the 12 is because r is an annual rate). Assume that your investments earn a 
return of r = 0.04 (4%).
5. Assume your annual salary is annual_salary.
6. Assume you are going to dedicate a certain amount of your salary each month to saving for 
the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1
for 10%). 
7. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your monthly salary (annual salary / 12).

"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))      # amount dedcated to saving each month from monthly salary
total_cost = float(input("Enter the cost of your dream home: "))                              # cost of your dream home
portion_down_payment = .25                                                                    # portion of total_cost needed for down payment
down_payment = portion_down_payment * total_cost
current_savings = 0                                                                           # amount saved thus far
r = .04                                                                                       # return on investment
monthly_salary = annual_salary / 12

months = 0
while current_savings < down_payment:
    current_savings += (current_savings * (r/12))                                             # we receive current_savings * r/12 at the end of each month
    current_savings += (portion_saved * monthly_salary)                                       # the portion of our monthly salary added to current_savings
    months += 1

print(f"Months: {months}")
