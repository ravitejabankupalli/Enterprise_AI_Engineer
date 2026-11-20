# ##EMI Calculator
# # First Version of EMI calculator in Python
# principal_amount= float(input("Enter the principal amount: "))
# annual_interest_rate= float(input("Enter the annual interest rate (in %): "))
# loan_tenure_years= int(input("Enter the loan tenure (in years): "))

# monthly_interest_rate= annual_interest_rate / (12 * 100)
# number_of_payments= loan_tenure_years * 12

# emi= (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
# print(f"The Equated Monthly Installment (EMI) is: {emi:.2f}")


# Second Version of EMI calculator in Python with Try and exception blocks as shown below
	##EMI Calculator

def get_number(prompt,error_message,convert=float):

	while True:

		try:
			return convert(input(prompt))

		except ValueError:

			print(error_message)

principal_amount=get_number(
	prompt="Enter Principal Amount: ",
	error_message="Please Principal Amount in Numbers Only!!"
	)
annual_interest_rate=get_number(
	prompt="Enter Annual Intrest Rate: ",
	error_message="Please Annual Intrest Rate in Numbers Only!!"
	)
loan_tenure_years=get_number(
	prompt="Enter Loan Tenure: ",
	error_message="Please Loan Tenure in Numbers Only!!"
	)
try:
	monthly_interest_rate= annual_interest_rate / (12 * 100)
	number_of_payments= loan_tenure_years * 12
	emi= (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
	print(f"The Equated Monthly Installment (EMI) is: {emi:.2f}")

except ValueError as e:
	print("There is something wrong in the code")
	print(f"The Error is as follows: \n{e}",e)
	print("vales:",repr(principal_amount),repr(annual_interest_rate),repr(loan_tenure_years))

except TypeError as e:
	print("The error is: ",e)


# while True:
	
# 	try:
# 		principal_amount= float(input("Enter the principal amount: "))
# 		break

# 	except ValueError:
# 		print("Please enter number only for principal amount")

# while True:

# 	try:
# 		annual_interest_rate= float(input("Enter the annual interest rate (in %): "))
# 		break

# 	except ValueError:
# 		print("Please enter number only for annual interst")


# while True:

# 	try:
# 		loan_tenure_years= int(input("Enter the loan tenure (in years): "))
# 		break

# 	except ValueError:
# 		print("Please enter number only for Loan Tenure Years")

