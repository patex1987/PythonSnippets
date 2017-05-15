'''
Created on 15. 5. 2017

@author: patex1987

We would like to create a program that will automatically approve
requests for loans.

The program should collect the information about:
A. Employment contract:
        1. Employee has contract
        2. Employee is in probation period

B. Requester's income balance
        1. net income
        2. amount of money paid in regular monthly payments

C. Employee education (1-basic,2-high school, 3-university)

D. Requester's citizenship
        1. Employees is country's National

E. Number of months in which the loan will be paid

And the decision rules are:

* We borrow with interest of 2.5%.
* Total amount to be paid back to our bank is calculated as loan + interest.
* Monthly payment is calculated as the total amount to be paid back divided by
the number of the months in which the loan will be paid

We do not give loans to those in probation period and unemployed.

Then we give loan under the following conditions:

For Czech nationals:
1. the money left after all payments executed, have to be
more than 2.5 times more than the Monthly payment

2. if the amount of money left after executing all payments is
between 2.5 to 2 times more than the Monthly payment
 - the requester cannot be in probation period

3. if the amount of money left after executing all payments is
between 2 to 1.5 times more than the Monthly payment
- the requester cannot be in probation period and has to be university educated

For other nationals:
1. the money left after all payments executed, have to be
more than 3 times more than the Monthly payment.

2. if the amount of money left after executing all payments is
between 3 to 2.5 times more than the Monthly payment
- the requester has to be university educated

'''


class Loan_Application(object):
    '''
    Class for loan application evidence and evaluation
    '''
    def __init__(self, employment_status,
                 income,
                 payment,
                 educational_level,
                 country_of_origin,
                 citizenship,
                 money_amount,
                 payment_duration):
        '''
        Class constructor
        '''
        self.employment_status = employment_status
        self.income = income
        self.payment = payment
        self.educational_level = educational_level
        self.country_of_origin = country_of_origin
        self.citizenship = citizenship
        self.money_amount = money_amount
        self.payment_duration = payment_duration
        self.application_passed = self.evaluate_application()
        self.money_left = self.income - self.payment
        self.interest = 0.025
        self.payback = self.calculate_total_payback(self.interest)

    def evaluate_application(self):
        '''
        Internal method for application evaluation
        '''
        monthly_payment = self.money_amount / self.payment_duration
        if self.citizenship:
            if self.money_left < (1.5 * monthly_payment):
                return False
            elif self.money_left >= (1.5 * monthly_payment) and \
                    self.money_left < (2.0 * monthly_payment):
                if self.employment_status == "P":
                    return False
                if self.educational_level != "3":
                    return False
            elif self.money_left >= (2.0 * monthly_payment) and \
                    self.money_left < (2.0 * monthly_payment):
                if self.employment_status == "P":
                    return False
        elif not self.citizenship:
            if self.money_left < (2.5 * monthly_payment):
                return False
            elif self.money_left >= (2.5 * monthly_payment) and \
                    self.money_left < (3.0 * monthly_payment):
                if self.educational_level != "3":
                    return False
        return True

    def calculate_total_payback(self, interest):
        '''
        amount + interest
        '''
        return (1 + interest)*self.money_amount


def prompt_employment():
    '''
    Prompts the applicant for its employment status
    '''
    while True:
        print("What is Your employment status?")
        employment_state = input(
            "[U - unemployed / P - probation / C - contract]: ")
        enabled_states = list("UPC")
        if employment_state.upper() not in enabled_states:
            print("Unknown employment state")
            continue
        return employment_state


def prompt_income_payments():
    '''
    Prompts the applicant for its income and payments
    '''
    while True:
        income_balance = input("Enter Your monthly average income: ")
        try:
            if int(income_balance) > 0:
                break
        except ValueError:
            print("Income should be a number")
    while True:
        regular_payments = input("Enter Your monthly payments: ")
        try:
            if int(regular_payments) > 0:
                return int(income_balance), int(regular_payments)
        except ValueError:
            print("Payment should be a number")


def prompt_employee_education():
    '''
    Prompts the application for its degree of education
    '''
    while True:
        print("What is Your highest education level?")
        education_level = input(
            "[1 - basic,2 - high school, 3 - university]: ")
        enabled_levels = list("123")
        if education_level not in enabled_levels:
            print("Not allowed education level")
            continue
        return education_level


def prompt_citizenship():
    '''
    Prompts the applicant for its country of origin
    '''
    while True:
        country_origin = input("What is Your country of origin?: ")
        if not country_origin.isalpha():
            print("The country should consist of letters")
            continue
        break
    while True:
        citizenship = input("Are You a citizen of this country? [Y/N]: ")
        answers = list("YN")
        if citizenship.upper() not in answers:
            print("Wrong answer")
            continue
        if citizenship.upper() == "Y":
            citizenship = True
        elif citizenship.upper() == "N":
            citizenship = False
        return country_origin, citizenship


def prompt_amount():
    '''
    Prompts the user for the amount of loan
    '''
    while True:
        money_amount = input("How much money do you want to borrow?: ")
        try:
            if int(money_amount) > 0:
                return int(money_amount)
        except ValueError:
            print("You should enter a positive number")
            continue


def prompt_payment_duration():
    '''
    Prompts the user for the loan duration
    '''
    while True:
        duration = input("How long do You want to pay the loan? [months]: ")
        try:
            if int(duration) > 0:
                return int(duration)
        except ValueError:
            print("You should enter a positive number")
            continue


def main():
    '''
    The main loop of the program
    '''
    employment_status = prompt_employment()
    income, payment = prompt_income_payments()
    education_level = prompt_employee_education()
    country_of_origin, citizenship = prompt_citizenship()
    money_amount = prompt_amount()
    payment_duration = prompt_payment_duration()
    loan_application = Loan_Application(employment_status,
                                        income,
                                        payment,
                                        education_level,
                                        country_of_origin,
                                        citizenship,
                                        money_amount,
                                        payment_duration)
    if loan_application.application_passed:
        print("You are fulfilling all the requirements for the loan")
    elif not loan_application.application_passed:
        print("You are not fulfilling the requirements")

if __name__ == '__main__':
    main()
