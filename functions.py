import datetime as dt

def calculate_loan(budget):

    ONEMONTH_LOAN = 655
    should_have_loan = 0

    month = int(dt.datetime.now().strftime("%m"))
    if 0 < month < 6:
        leftover_months = 6 - month - 1
    else:
        leftover_months = 12 - month - 1

    should_have_loan = leftover_months * ONEMONTH_LOAN

    current_day = int(dt.datetime.now().strftime("%d"))
    should_have_loan += (ONEMONTH_LOAN / 30) * (30 - current_day)

    result = round(budget - should_have_loan, 2)

    return result


if __name__ == "__main__":
    print(calculate_loan(2000))


