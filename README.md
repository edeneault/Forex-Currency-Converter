# Forex Currency Converter - Assesssment 3 - SpringBoard
<sup>by: Etienne Deneault</sup>


#### Files
* ``base.html - forex_converter.html - forex_conversion.html - analysis.html - app.py - utils.py - app.css - app.js - test_app.py - requirements.txt - README.MD - conceptual.md``


#### Features

* Main Function:  convert currency from one denomination to another based on current exchange rate. Output: conversion amount.
* On request, the user can access additional details/analysis of the conversion.
    * Data Points Available:
        * Conversion Amount
        * Conversion Rate
        * 30 Days Past - Conversion Amount Delta (%)
        * 1 Year Past - Conversion Amount Delta (%)
        * 5 Years Past - Conversion Amount Delta (%)
        * 10 Years Past - Conversion Amount Delta (%)
        * Conversion Amount Estimate - at bank, atm, credit card and kiosk.
        * Count of Conversions performed by user.
* Tested with Python unittest.  (unit and integration tests)
* Line Chart Visual Representation of the currency fluctuation over time.
* Bootstrap 4.5 Responsive Behavior.

#### Code Details

* ``HTML`` is structured using flask templates. The structure is *nested*.
* ``app.py`` contains the app routes.
* ``utils.py`` contains data request functions, data analysis functions an helper functions.  Included in ``utils.py`` is a commmented section with a test for each function. 
* ``app.js`` handles the canvas line chart.  
* ``app.css`` provides basic styling.

#### Todos and Improvements

* Improved Documentation: Implentation of doctests with already created tests from the commented section in ``utils.py``.
* Implement a route to provide the reverse the ``to_county`` and ``from_country`` conversion values upon clicking the "double arrow" *fontawesome icon*.
* Refactor ``utils.py`` into OOP, it would optimize how information is delivered to the routes and facilitate storing conversion transaction states.
* Create more *edge case* tests.
* Create mote *specific* flash messages.
* Use a *less hacky* method to pass data to javascript.
* Include *spinner* buttons to improve user experience.
* Acuracy of the conversions is rounded to 2 decimal points, calculations are based on 10 decimal points.  Currently, the rounding is in *favor* of the *conversion service provider*.

#### Process && Learnings

* I set the following goals at the beginning of the project:
    * Take a *Data Science* approach to the application favoring functionality, data and data anlysis over UI-UX.
    * Use OOP for model. (did not get to this yet)
    * Create a good level of *robutness* to the application.
    * Persist the "state".
    * Create tests for all functions and precesses.
    * Create appropriate Documentation.

* Line Chart: Assessment specs said "no js" but I decided to include this feature anyhow since it was not part of the core requirements. I could re-do using mathoplib or bokeh modules in Python but that would take about a "day" to accomplished ( I have done this before for a capstone project ).


#### Technologies && Third Party Libraries && Fonts

* Python, flask, HTML, CSS, JS, jQuery


#### Time Log

03-05-2021:
* 15 min. - First Read 

03-06-2021
* 20 min. - Read Docs Forex Module
* 45 min. - Planning in Engineering Notebook
* 45 min. - Project set-up and experimentation with forex module
* 30 min. - basic mark-up templates
* 120 min. - build functions in utils to access api data and create functionality functions
* 240 min. - build routes and application logic/flow-data control
* 60 min. - refinement of analysis functions
* 120 min - integration of line chart

03-07-2021
* 120 min. - error checking and flash messages
* 120 min. - code clean-up and minor improvements
* 60 min. - complete the conceptual.md document 

03-09-2021
* 60 min. - build a README.md document
* 15 min. - update git/github

Total ~ 17 hrs and 50 minutes


#### Sources && References

* Code Base provided by SpringBoard - Forex Assessment 3

* Documentation Used: python docs, flask docs, StackOverflow, jQuery, MDN, bootstrap docs

* Media: image is expressively allowed to be used for a nonmonetary purpose.