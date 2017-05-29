#!/usr/bin/env python3
__taskuid__ = ''
'''
Everybody, who is going to take a mortgage would like to know, whether
the payments and interests are calculated well.

There is some obscure magic behind the calculation and it is hard to
reverse engineer the way, how our bank really calculated the payments.

Fortunately, we can make our own calculator, that will print nicely
our monthly payments.

Or maybe we would like to know, what is the total amount of money, we will
have to pay to our bank. Our calculator should do that as well.

Your task will be to create a program that will print out the following:

| Loan: 2000000 | Years: 30 | Interest: 693880 | Monthly Payment: 7483 |
========================================================================
|    Payment    |  Interest |    Principal     |      Left to Pay      |
========================================================================
|       1       |   4,692   |      2,791       |       2,693,880       |
|       2       |   4,679   |      2,804       |       2,686,397       |
|       3       |   4,666   |      2,817       |       2,678,914       |
|       4       |   4,653   |      2,830       |       2,671,431       |
|       5       |   4,640   |      2,843       |       2,663,948       |
|       6       |   4,627   |      2,856       |       2,656,465       |


The inputs into the program are:

1. The amount of money lent = Loan
2. Number of years in which the mortgagte will be paid = years
3. Monthly interest rate offered by the bank (e.g. 2.09%)

In order we can present the above output, the program will then have to
calculate/generate:

1. Monthly payment we will have to send to our bank:

        monthly_payment = L*(r * (1 + r)**n) / ((1 + r)**n-1)

        where:

        L - is the amount of money we are borrowing
        r - is the interest rate that bank offers us (e.g. 2.09%) - should be
            converted into decimal number => 0.0209 and divided by 12 as this
            is yearly interest rate:

            r = yearly_rate / 100 / 12

        n - is the number of months in which we will pay our mortgage (when
            talking to the bank, we say - I want it for 20 years for example
            - they convert it into number of months)

2. Total amount of money that we will have to pay to the bank

    total_amount = monthly_payment * number_of_months

3. Total interest, that we will pay to the bank

    total_interest = total_amount - loan

4. The listing of individual monthly payments decomposed into
    a)payment number (from 1 until the last month's number)
    b)interest part = the amount the bank is earning for lending us money.

        It has to be calculated for every single month as follows:

        monthly_interest = L * r

        L - is the amount of money that is left to be paid
        r - is the monthly interest rate converted from the yearly
            interest rate that bank offers us (e.g. 2.09% -> 2.09 / 100 / 12)

    c)principal part = the amount of money we pay to actually lower our debt

        monthly_payment - monthly_interest

        At the beginning interest part is high, and principal quite low.
        However, with each payment, the debt is lowered every month a and
        monthly interest rate is lower and lower, the monthly payment is
        constant and therefore principal is higher and higher.

    d)the total amount of money to be still paid

'''


# this function will require the special formula listed in the task description
# to calculate the monthly payment
def calculate_monthly_payment(loan, monthly_rate, num_periods):
    '''
    monthly_payment = L*(r * (1 + r)**n) / ((1 + r)**n-1)
    '''
    return loan*(monthly_rate*(1+monthly_rate)**num_periods) / \
        ((1+monthly_rate)**num_periods-1)


# the following function should just calculate the total mortgage
def calculate_total_mortgage(monthly_payment, num_periods):
    '''
    total_amount = monthly_payment * number_of_months
    '''
    return monthly_payment * num_periods


# the following function should just calculate the total interest
def calculate_total_interest(mortgage, loan):
    '''
    Calculates the amount of total interest
    '''
    return mortgage - loan


# to calculate installments you will need the amount of money borrowed,
# number of months and interest rate - with that you can calculate the rest
def calculate_payments(loan, monthly_rate, num_periods,
                       monthly_payment, total_amount, total_interest):
    '''
    This function returns a collection of monthly changes in interests and
    principals
    '''
    # generate a collection of payments in order the print_instalments
    # function can print it
    payments = list()
    # you will probably need to calculate monthly payment and total amount
    # to be paid, before you begin to generate the collection

    # now you can begin to generate the overview of payments
    # do not forget to recalculate the monthly interest rate for each month
    # in order it is lowered each month and principal is increased
    # also do not forget to discount the total amount left to be paid (interest
    # + loan)
    total_amount_left = total_amount
    for i in range(num_periods + 1):
        interest_part = monthly_rate * total_amount_left
        principal_part = monthly_payment - interest_part

        payments.append((i+1,
                         round(interest_part, 2),
                         round(principal_part, 2),
                         round(total_amount_left, 2)))
        total_amount_left -= monthly_payment
    # return the overview of payments as a list of tuples:
    # [(month_num,interest,principal,left_to_pay),(month_num,interest,principal,
    # left_to_pay), etc.]
    return payments


def find_max_length(words):
    '''
    Finds the longest word, in order to find basis for word padding
    '''
    return max([len(word) for word in words])


def generate_header(loan, num_periods, total_interest, monthly_payment):
    '''
    Generates a list of header strings
    '''
    # Loan: 2000000 | Years: 30 | Interest: 693880 | Monthly Payment: 7483
    words = []
    words.append("Loan: {0}".format(loan))
    words.append("Years: {0}".format(num_periods // 12))
    words.append("Interest: {0:0.2f}".format(total_interest))
    words.append("Monthly payment: {0:0.2f}".format(monthly_payment))
    return words


def generate_string(words, max_length):
    '''
    Generates pretty string from a sequence
    '''
    inner = "|".join(["{0:^{1}}".format(word, max_length) for word in words])
    return "|{0}|".format(inner)


# to print installments you will need the amount of money borrowed,
# number of months and interest rate - with that you can calculate the rest
def print_instalments(loan, monthly_rate, num_periods):
    '''
    This function prints out all the necessary information about Your mortgage
    '''
    # you will probably need to calculate monthly payment and total amount
    # to be paid, total interest, and generate the collection of monthly
    # payments before you begin to print the report
    monthly_payment = calculate_monthly_payment(loan,
                                                monthly_rate,
                                                num_periods)
    total_amount = calculate_total_mortgage(monthly_payment, num_periods)
    total_interest = calculate_total_interest(total_amount, loan)
    payments = calculate_payments(loan,
                                  monthly_rate,
                                  num_periods,
                                  monthly_payment,
                                  total_amount,
                                  total_interest)
    # think about how those 2 headers can be printed, in order the column
    # widths are equal - you will probably need to use:
    # > string formatting methods or
    # > string formatting expressions
    # surely you will want to find the optimal length of a row in order
    # everything enters on each row
    header_words = generate_header(loan,
                                   num_periods,
                                   total_interest,
                                   monthly_payment)
    max_length = find_max_length(header_words)
    max_length += 2
    # now you can print the the individual rows for each payment
    print(generate_string(["-"*max_length]*4, max_length))
    print(generate_string(header_words, max_length))
    print(generate_string(["-"*max_length]*4, max_length))
    column_names = ["Payment", "Interest", "Principal", "Left to pay"]
    print(generate_string(column_names, max_length))
    print(generate_string(["-"*max_length]*4, max_length))
    for payment in payments:
        print(generate_string(payment, max_length))
    print(generate_string(["-"*max_length]*4, max_length))
    # Payment    |  Interest |    Principal     |      Left to Pay
    # Loan: 2000000 | Years: 30 | Interest: 693880 | Monthly Payment: 7483

if __name__ == '__main__':
    LOAN = 800000
    MONTHLY_RATE = 2.09/100/12
    NUM_PERIODS = 30*12

    print_instalments(loan=LOAN,
                      monthly_rate=MONTHLY_RATE,
                      num_periods=NUM_PERIODS)
