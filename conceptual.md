### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    * Python: variable naming convention - ``like_this`` (js: ``likeThis``)
    * Python: no keyword for variable decleration (js: ``let``, ``var``, ``const``)
    * Python: indentation delineates *scope/blocks* - javacript uses ``{ }``
    * Python: equality == (*strict about types*), thruthiness ``[1, 2, 3] == [1, 2, 3]`` #true, ``[1, 2, 3] is [1, 2, 3]`` #false
    * Python: ``and`` , ``or`` , ``not`` (js: ``&&`` , ``||`` , ``not``)
    * Python: for in loop, like js for of loop - ``range()``, ``enumerate()`` used for indexed iteration
    * Python: functions will not accept additional arguments and do not explicitely ``return`` return ``None``
    * Python: has docstrings for built in documentation ``dir()``
    * Python: comments ``#``, js: ``/`` 

    <br>

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

    1. ``c = my_dict.get("c", 0)``
    2. ``key = "c" if key in my_dict: c = myDict.get("c") return c``

    <br>


- What is a unit test?
    * Unit tests are to test code in isolated small pieces
    <br>
- What is an integration test?
    * Integration tests are used to test combined program units.  Program units are tested in multiple ways.
    <br>
- What is the role of web application framework, like Flask?
    * Frameworks make it easier to reuse code for common HTTP operations and to structure projects so other developers with knowledge of the framework can quickly build and maintain the application.
    <br>
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    * One way is not better than the other, it depends on the situation. For example: the object itself could be passed as a url parameter, while it's content descriptors as query params like so: ``/conversion/conversions?country_from=USD``  Also, passing through the url route allows to capture the object/variable and pass it as an argument in the function, like so: 
    ``@app.route("/conversion/<country_from>")``
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``def conversion_view(country_from):``
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``return country_from``
    <br>
- How do you collect data from a URL placeholder parameter using Flask?
    * The example above demonstrates how to do this.  In addition, it can be useful to increment an index by setting the variable to a start value and then incrementing it within the route function.
    <br>
- How do you collect data from the query string using Flask?
    * Using ``request.args``, like so: ``to_country = request.args["to-country"]``
    <br>
- How do you collect data from the body of the request using Flask?
    * Using ``request.data.get()``, like so: `` lat = request.data.get("lat", "") ``
    <br>
- What is a cookie and what kinds of things are they commonly used for?
    * Cookies are a way to store small bits of info on client (browser).
    * Cookies are name/string-value pair stored by the client (browser).
    * Used to maintain "state".
- What is the session object in Flask?
    * Uses Cookies to function.
    * Flask sessions are a “magic dictionary”.
    * Contain info for the current browser.
    * Preserve type (lists stay lists, etc).
    * Users con't modify data.
    <br>
- What does Flask's `jsonify()` do?
    * jsonify is a function in Flask's flask.json module. jsonify serializes data to JavaScript Object Notation (JSON) format, wraps it in a Response object with the application/json mimetype.
