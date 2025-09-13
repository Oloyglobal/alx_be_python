monthly_income = float(input("enter your monthly income: "))
monthly_expenses = float(input("enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
print(f"Your monthly savings ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")