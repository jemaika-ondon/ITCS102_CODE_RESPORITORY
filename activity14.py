#age(integer)
#is_employed(boolean)
#credit_score(integer)
#annual_income(float)
#has_collateral(boolean)

age = int(input('Enter Your Age: '))
is_employed = bool(input('Are you employed?: '))
credit_score = int(input('Enter Your Credit Score: '))
annual_income = float(input('How much is your annual income?: '))
has_collateral = bool(input('Do you have collateral?: '))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print('Applicant pass baseline requirement')
    if credit_score >= 750:
        print('You have a high credit score')
        if annual_income >= 100000:
            base_rate = 5.0
            print('You have a high salary and high credit score, your interest rate is', base_rate)
        else:
            base_rate = 4.5
            print('You have a high salary and high credit score, your interest rate is', base_rate')
    elif credit_score 
    else:
        print('Rejected: Fails Tier1 requirements')
else:
    print('Rejected: Fails baseline criteria')