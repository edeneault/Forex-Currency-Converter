# from flask import Flask, request, render_template, session, jsonify
import os
from forex_python.converter import *

import json
from decimal import *
import time
from datetime import datetime, date, time, timedelta


# Currente date --- no time format Output example: "2021-03-06" ###
date_object = date.today()
### Current date and time --- format Output example: "2021-03-06 07:25:27.655038" ###
date_obj = datetime.now()
### Test Date Obj ###
date_obj_test_date = datetime(2021, 1, 1, 18, 36, 28, 151012)

### Decimal Context arguments ###
getcontext().prec = 10

### CURRENCY RATES INSTANCES ###
c = CurrencyRates()
c_dec = CurrencyRates(force_decimal=True)
c_codes = CurrencyCodes()

#### CURRENCY CONVERTER FUNCTIONS ####


def conv_rates(ctry):
    """ returns dict with current country conversion rates with all other available currencies """
    conv_rates = c.get_rates(ctry)
    return conv_rates


def conv_rates_date(ctry):
    """ returns dict with country conversion rates with all other available currencies
    on a -- specific date --"""
    conv_rates_date = c.get_rates(ctry, date_obj)
    return conv_rates_date


def conv_rate_ctry1_ctry2(ctry1, ctry2):
    """ returns type float with country1 to country2 --current-- currency conversion rate """
    conv_rates_ctry1_ctry2 = c.get_rate(ctry1, ctry2)
    return Decimal('%.4f' % (conv_rates_ctry1_ctry2))


def conv_rate_ctry1_ctry2_date(ctry1, ctry2, date):
    """ returns type float with country1 to country2 --specified date-- currency conversion rate """

    conv_rates_ctry1_ctry2_date = c.get_rate(ctry1, ctry2, date)
    return conv_rates_ctry1_ctry2_date


def conv_amt_ctry1_ctry2(ctry1, ctry2, amt):
    """ returns type float with country1 to country2 --current date/time-- conversion amount """
    conv_amt_ctry1_ctry2 = c.convert(ctry1, ctry2, amt)
    return conv_amt_ctry1_ctry2


def conv_amt_ctry1_ctry2_date(ctry1, ctry2, amt, date):
    """ returns type float with country1 to country2 --current date/time-- conversion amount """
    conv_amt_ctry1_ctry2_date = c.convert(ctry1, ctry2, amt, date)
    return conv_amt_ctry1_ctry2_date


def conv_amt_ctry1_ctry2_decimal(ctry1, ctry2, amt):
    """ returns type float with country1 to country2 --current date/time-- conversion amount decimal: 2 """
    conv_amt_ctry1_ctry2_decimal = c_dec.convert(ctry1, ctry2, Decimal(amt))
    # print(Decimal(conv_amt_ctry1_ctry2_decimal))
    # return "{:.2f}".format(conv_amt_ctry1_ctry2_decimal)
    return Decimal(conv_amt_ctry1_ctry2_decimal).quantize(Decimal('.01'), rounding=ROUND_DOWN)


def conv_amt_ctry1_ctry2_detect(ctry1, ctry2, amt):
    """ returns type float with country1 to country2 --current date/time-- conversion amount decimal: 2 """
    conv_amt_ctry1_ctry2_detect = c.convert(ctry1, ctry2, amt)
    return conv_amt_ctry1_ctry2_detect


def currency_get_symbol(ctry):
    """ returns currency symbol """
    currency_symbol = c_codes.get_symbol(ctry)
    return currency_symbol


def currency_get_name(ctry):
    """ returns currency name"""
    currency_name = c_codes.get_currency_name(ctry)
    return currency_name


def currency_codes():
    """ returns list on currency codes """
    dict = conv_rates("USD")
    currency_codes = list(dict.keys())
    return currency_codes

### ANALYSSIS FUNCTIONS###


def date_to_date(ctry1, ctry2, amt, date):
    """ returns year to date (%) gain/loss """
    current_val = conv_amt_ctry1_ctry2(ctry1, ctry2, amt)
    start_year_val = conv_amt_ctry1_ctry2_date(ctry1, ctry2, amt, date)
    result = percentage_delta(current_val, start_year_val)
    return result


def conv_inst_fees_amount(institution, amount):
    """ returns a new conversion amount after est. fees added by type of instution used for transaction """
    inst_switcher = {'bank': 0.02, 'atm': 0.02,
                     'credit': 0.03, 'kiosk': 0.05}
    rate = inst_switcher.get(institution, "Invalid Institution")
    amount = float(amount)
    return Decimal('%.2f' % (amount - (amount * rate)))


def percentage_delta(part, whole):
    """ returns delta percentage of "part" and "whole" values """
    delta_percentage = 100 * float(part)/float(whole) - 100
    return Decimal('%.2f' % (delta_percentage * 1000 / 1000))


### DATE PARSERS FUNCTIONS - todo:  combine into one function ###

def date_one_year_past():
    """ returns date object of the date ONE year in the past """
    date_string = f"{datetime.now() - timedelta(days=1*365)}"
    date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
    return date_obj


def date_one_month_past():
    """ returns date object of the date ONE month in the past """
    date_string = f"{datetime.now() - timedelta(days=1*30)}"
    date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
    return date_obj


def date_five_years_past():
    """ returns date object of the date ONE month in the past """
    date_string = f"{datetime.now() - timedelta(days=5*365)}"
    date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
    return date_obj


def date_ten_years_past():
    """ returns date object of the date ONE month in the past """
    date_string = f"{datetime.now() - timedelta(days=10*365)}"
    date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
    return date_obj

### UTILITY FUNCTION(S) ###


def is_number(amount):
    try:
        float(amount) or int(amount)
        return True
    except ValueError:
        return False


### List of currency codes ###
curr_codes_list = currency_codes()


#### FUNCTION OUTPUTS  ######
#### UNCOMMENT BELOW TO VIEW FUNCTIONS AND TESTS ####
#### Create doctests for each function for more complete documentation ####
print(getcontext())
print()
print("Currency Conversion Rates for - specified country - Current")
print("__________________________________________________________________")
print(conv_rates("USD"))
print()
print("Currency Conversion Rates  for - specified country - Specified Date")
print("__________________________________________________________________")
print(conv_rates_date("USD"))
print()
print("Currency Conversion Rate - Country to Country - current")
print("__________________________________________________________________")
print(conv_rate_ctry1_ctry2("USD", "CAD"))
print()
print("Currency Conversion Rate - Country to Country - Specified Date")
print("__________________________________________________________________")
print(conv_rate_ctry1_ctry2_date("USD", "CAD",
                                 date_obj_test_date), date_obj_test_date)
print()
print("Currency Conversion Amount - Country to Country - current ")
print("__________________________________________________________________")
print(conv_amt_ctry1_ctry2("USD", "CAD", 10.25))
print()
print("Currency Conversion Amount - Country to Country - Specified Date")
print("__________________________________________________________________")
print(conv_amt_ctry1_ctry2_date("USD", "CAD", 10,
                                date_obj_test_date), date_obj_test_date)
print()
print("Currency Conversion Amount - Country to Country - current - Decimal 2")
print("__________________________________________________________________")
print(conv_amt_ctry1_ctry2_decimal("USD", "INR", 10.25))
print()
print("Currency Conversion Amount - Country to Country - current - Detect decimal")
print("__________________________________________________________________")
print(conv_amt_ctry1_ctry2_detect("USD", "INR", Decimal('10.25')))
print()
print("Currency Symbol")
print("__________________________________________________________________")
print(currency_get_symbol('GBP'))
print()
print("Currency Name")
print("__________________________________________________________________")
print(currency_get_name("EUR"))
print()
print("Currency Codes - returns list")
print("__________________________________________________________________")
print(currency_codes())
print(currency_codes()[0])
print()
print("Year to Date: (%) GAIN/LOSS")
print("__________________________________________________________________")
print(date_to_date("CAD", "USD", 100, date_obj_test_date))

print()
print("One Year Ago - find date")
print("__________________________________________________________________")
print(date_one_year_past())
print()
print("One Month Ago - find date")
print("__________________________________________________________________")
print(date_one_month_past())
print()
print("five Year Ago - find date")
print("__________________________________________________________________")
print(date_five_years_past())
print()
print("tenYear Ago - find date")
print("__________________________________________________________________")
print(date_ten_years_past())
print()
print("Conversion with Fees - based on institution type input and conversion amount")
print("__________________________________________________________________")
print(conv_inst_fees_amount('atm', 78.74))
print()
print("Check if request amount is a number")
print("__________________________________________________________________")
print(is_number(''))
print()


# ### OBJECT VALUE TESTING ###
# print("#### OBJECT VALUE TESTING ####")
# print("__________________________________________________________________")
# print(date_obj)
# print(date_object)
# print(date_obj_test_date)
# print("{:.2f}".format(1.25555))
# print(Decimal("{:.2f}".format(1.25555)))
# print(Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN))
