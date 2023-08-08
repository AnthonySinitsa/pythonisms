# pythonisms

What is a dunder method?

Dunder methods are special methods in Python

Also known as  double underscore methods or magic methods

Allow for customizing built-in functions

Surrounded by double underscores, for example:  __init__

What can it do?

Customizes built-in functions/methods or custom functions

Allows devs to define how objects of a class should behave in response to operations, including:
Addition
Subtraction
String representation

For example, __str__
Customizes the string representation of an object when converted  by the str() function or through string interpolation

Why use dunder methods?

Customize built-in behavior

Create consistency with built-in types

Overload operators for custom objects (helps with readability, comparing and ordering, etc.)

Make code more readable

Allow for interoperability (compatible with various libraries and built-ins)

    pytest tests/test_pythonisms.py
