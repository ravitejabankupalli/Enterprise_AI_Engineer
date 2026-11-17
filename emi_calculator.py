##EMI Calculator
principal_amount= float(input("Enter the principal amount: "))
annual_interest_rate= float(input("Enter the annual interest rate (in %): "))
loan_tenure_years= int(input("Enter the loan tenure (in years): "))

monthly_interest_rate= annual_interest_rate / (12 * 100)
number_of_payments= loan_tenure_years * 12

emi= (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
print(f"The Equated Monthly Installment (EMI) is: {emi:.2f}")