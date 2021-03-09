from unittest import TestCase
from app import app
from flask import session
from utils import *

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):
    """ Unit and Integration Tests"""

    def test_converter_view(self):
        """ Test converter view"""
        print("in converter_view")
        with app.test_client() as client:

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertIn('curr_codes_list', session)
            self.assertIn('conversions', session)
            self.assertIn('from-country', session)
            self.assertIn('to-country', session)
            self.assertIn('amount', session)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(' <form id="conversion-form"', html)
            self.assertIn(
                ' <div class="text-light text-left small text-light">Session Conversion Count', html)

    def test_conversion_view(self):
        """ Test conversion view"""
        print("in conversion_view")
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['from-country'] = 'USD'
                change_session['to-country'] = 'AUD'
                change_session['amount'] = '100'

            resp = client.get(
                '/conversion?from-country=USD&to-country=AUD&amount=100')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                '<div class="header text-light">CONVERSION RESULT</div>', html)

    def test_analysis_view(self):
        """ Test conversion view"""
        print("in converter_view")
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['from-country'] = 'AUD'
                change_session['to-country'] = 'AUD'
                change_session['amount'] = '1'
            from_country = 'AUD'
            to_country = 'AUD'
            amount = '1'

            conv_result = conv_amt_ctry1_ctry2_decimal(
                from_country, to_country, amount)
            symbol_to_country = currency_get_symbol(to_country)
            name_to_country = currency_get_name(to_country)
            symbol_from_country = currency_get_symbol(from_country)
            name_from_country = currency_get_name(from_country)
            past_one_year = date_one_year_past()
            past_one_month = date_one_month_past()
            past_five_years = date_five_years_past()
            past_ten_years = date_ten_years_past()

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
            conv_result_credit = conv_inst_fees_amount(
                'credit', conv_result)
            data = {'10y': str(ten_year_delta), '5y': str(five_year_delta),
                    '1y': str(year_delta), '1m': str(month_delta), 'now': str(0)}

            resp = client.get('/analysis')
            html = resp.get_data(as_text=True)
            self.assertEqual(amount, '1')
            self.assertEqual(to_country, 'AUD')
            self.assertEqual(from_country, 'AUD')
            self.assertEqual(conv_result, Decimal('1.00'))
            self.assertEqual(conv_rate, Decimal('1.0000'))
            self.assertEqual(month_delta, Decimal('0.00'))
            self.assertEqual(year_delta, Decimal('0.00'))
            self.assertEqual(five_year_delta, Decimal('0.00'))
            self.assertEqual(ten_year_delta, Decimal('0.00'))
            self.assertEqual(conv_result_bank, Decimal('0.98'))
            self.assertEqual(conv_result_atm, Decimal('0.98'))
            self.assertEqual(conv_result_credit, Decimal('0.97'))
            self.assertEqual(conv_result_kiosk, Decimal('0.95'))
            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                '<i class="fas fa-arrow-alt-circle-right green"></i>', html)
            self.assertIn(
                '<canvas id="chLine" height="100">', html)
