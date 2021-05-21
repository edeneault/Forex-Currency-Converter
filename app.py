from flask import Flask, request, render_template, session, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime, date, time
from decimal import *
# from forex_python.converter import CurrencyRates, CurrencyCodes
from utils import *

### App and Debbugger init ###
app = Flask(__name__)
app.config['SECRET_KEY'] = "not-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)


#### APP ROUTES #####


@app.route("/")
def forex_converter_view():
    """ Displays the forex converter UI View """
    try:
        curr_codes_list = currency_codes()
        session['curr_codes_list'] = curr_codes_list
        session['conversions'] = session.get("conversions", 0)
        session['from-country'] = session.get("from-country", 0)
        session['to-country'] = session.get("to-country", 0)
        session['amount'] = session.get("amount", 0)
        conversions = session.get("conversions", 0)
        return render_template("forex_converter.html", curr_codes_list=curr_codes_list, conversions=conversions)
    except:
        return render_template("forex_converter.html")


@app.route("/conversion")
def forex_conversion_view():
    """ Displays the forex conversion UI View """
    try:
        from_country = request.args["from-country"]
        to_country = request.args["to-country"]
        amount = request.args["amount"]

        session['from-country'] = from_country
        session['to-country'] = to_country
        session['amount'] = amount
        conversions = session.get("conversions", 0)
        session["conversions"] = conversions + 1

        curr_codes_list = sorted(currency_codes())
        conv_result = conv_amt_ctry1_ctry2_decimal(
            from_country, to_country, amount)
        symbol_to_country = currency_get_symbol(to_country)
        name_to_country = currency_get_name(to_country)
        symbol_from_country = currency_get_symbol(from_country)
        name_from_country = currency_get_name(from_country)
    except:
        if not (is_number(request.args["amount"])):
            flash(
                f"Please enter (currency types) and (amount) to convert (for example: USD, AUD, 5.5) INVALID(empty fields, alphabetic characters, special characters)")
            return redirect(f"/")

    return render_template("forex_conversion.html",
                           from_country=from_country,
                           to_country=to_country,
                           amount=amount,
                           conv_result=conv_result,
                           symbol_to_country=symbol_to_country,
                           name_to_country=name_to_country,
                           symbol_from_country=symbol_from_country,
                           name_from_country=name_from_country
                           )


@app.route("/analysis")
def show_conversion_analysis():
    """ Displays the conversion details and analysis"""

    ### RETREIVE TO MAINTAIN STATE ###
    from_country = session.get("from-country")
    to_country = session.get("to-country")
    amount = session.get("amount")
    conv_result = conv_amt_ctry1_ctry2_decimal(
        from_country, to_country, amount)
    symbol_to_country = currency_get_symbol(to_country)
    name_to_country = currency_get_name(to_country)
    symbol_from_country = currency_get_symbol(from_country)
    name_from_country = currency_get_name(from_country)

    ### DATE FINDER FUNCTIONS ###
    past_one_year = date_one_year_past()
    past_one_month = date_one_month_past()
    past_five_years = date_five_years_past()
    past_ten_years = date_ten_years_past()

    ### ANALYSIS DATA FUNCTIONS ###
    conv_rate = conv_rate_ctry1_ctry2(from_country, to_country)
    ten_year_delta = date_to_date(from_country, to_country,
                                  Decimal(amount), past_ten_years)

    five_year_delta = date_to_date(from_country, to_country,
                                   Decimal(amount), past_five_years)
    year_delta = date_to_date(from_country, to_country,
                              Decimal(amount), past_one_year)
    month_delta = date_to_date(from_country, to_country,
                               Decimal(amount), past_one_month)
    conv_result_bank = conv_inst_fees_amount('bank', conv_result)
    conv_result_atm = conv_inst_fees_amount('atm', conv_result)
    conv_result_kiosk = conv_inst_fees_amount('kiosk', conv_result)
    conv_result_credit = conv_inst_fees_amount('credit', conv_result)

    ###  DATA FOR CHART PLOT ###
    data = {'10y': str(ten_year_delta), '5y': str(five_year_delta),
            '1y': str(year_delta), '1m': str(month_delta), 'now': str(0)}
    # print(data)

    return render_template("analysis.html",
                           from_country=from_country,
                           to_country=to_country,
                           amount=amount,
                           conv_result=conv_result,
                           symbol_to_country=symbol_to_country,
                           name_to_country=name_to_country,
                           symbol_from_country=symbol_from_country,
                           name_from_country=name_from_country,
                           conv_rate=conv_rate,
                           ten_year_delta=ten_year_delta,
                           five_year_delta=five_year_delta,
                           year_delta=year_delta,
                           month_delta=month_delta,
                           conv_result_bank=conv_result_bank,
                           conv_result_atm=conv_result_atm,
                           conv_result_kiosk=conv_result_kiosk,
                           conv_result_credit=conv_result_credit,
                           data=data
                           )
