# Small Business Credit & Collateral Evaluator

#inputs
owner_age = int(input('Enter Your Age: '))
monthly_revenue = float(input('Enter Monthly Revenue: '))
credit_score = int(input('Enter Credit Score: '))
years_in_business = float(input('Enter Years in Business: '))
has_default = bool(eval(input('Enter If Have been Default (True / False): ')))
collateral_name = input('Enter Collateral Name:')
collateral_value = float(input('Enter Collateral Value: '))

max_loan = 0
base_fee = 0

# Outer Baseline Requirements
if owner_age >= 21 and years_in_business >= 2.0 and has_default == False:
    print('Baseline Requirements: PASSED')
    if credit_score >= 720:
        max_loan = 3 * monthly_revenue
        print('Maximum Loanable Amount is Set To: ',max_loan)
        if monthly_revenue >= 50000:
            base_fee = max_loan * 0.015
            print('APPROVED: Base Fee Rate is Set To: ', base_fee)
        else:
            base_fee = max_loan * 0.025
            print('APPROVED: Base Fee Rate is Set To: ',base_fee)

        # collateral
        if collateral_value >= max_loan:
            print('Collateral ',collateral_name, 'With A Value Of ', collateral_value, 'is ACCEPTED')
        else:
            print('REJECTED: Insufficient Collateral Value For',collateral_name)

        # Surcharge
        surge_fee = max_loan * base_fee
        print('Additional Charge: ',surge_fee)
        if max_loan % 5000 != 0:
            print('ADDITIONAL CHARGE ADDED')
            surge_fee += 250
            print('APPROVED: With Updated Base Fee: ',surge_fee)

    elif credit_score >= 620 and credit_score < 720:
        max_loan = 1.5 * monthly_revenue
        print('Maximum Loanable Amount is Set To: ',max_loan)
        if years_in_business >= 5.0:
            base_fee = max_loan * 0.02
            print('APPROVED: Base Fee Rate is Set To: ',base_fee)
        else:
            base_fee = max_loan * 0.035
            print('APPROVED: Base Fee Rate is Set To: ',base_fee)

        # collateral
        if collateral_value >= max_loan:
            print('Collateral ',collateral_name, 'With A Value Of ', collateral_value, 'is ACCEPTED')
        else:
            print('REJECTED: Insufficient Collateral Value For',collateral_name)
        
        # Surcharge
        surge_fee = max_loan * base_fee
        print('Additional Charge: ',surge_fee)
        if max_loan % 5000 != 0:
            print('ADDITIONAL CHARGE ADDED')
            surge_fee += 250
            print('APPROVED: With Updated Base Fee: ',surge_fee)

    else:
        print('REJECTED: Credit Score Below Requirement')
else:
    print('REJECTED: High Risk Application or Ineligible Owner')