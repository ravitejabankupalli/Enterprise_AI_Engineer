print('Welcome to Loan Eligibility Checker')
check='Yes'
while check=='Yes':
    name=input('Enter Your Name: ')
    age=int(input('Enter Your Age: '))
    income=float(input('Enter your monthly take home salary: '))
    credit_score=int(input('Enter your credit score: '))
    if age<=21 and age>=60:
        print(f'Sorry {name}, you are not eligible for a loan')
    elif income<21000:
        print(f'Sorry {name}, you are not eligible for a loan')
    elif credit_score<600:
        print(f'Sorry {name}, you are not eligible for a loan')
    else:
        print(f'Congratulations! {name} You are eligible for a loan')
    check=input('Do you want to check for another person? (Yes/No): ')