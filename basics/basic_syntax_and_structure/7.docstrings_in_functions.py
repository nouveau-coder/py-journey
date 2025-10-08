#another name for multiline comments is docstrings. Docstrings are used to document functions, classes and modules in python.
def example_function():
    '''
    this is a docstring for the example_function
    it can span multiple lines
    everything between the triple quotes is ignored by python
    this is useful for writing long comments or documentation
    '''
    print('this line of code will be executed')
example_function()
#we can also use triple double quotes for docstrings.
def another_example_function():
    """
    this is another docstring for the another_example_function
    it also spans multiple lines
    everything between the triple double quotes is ignored by python
    """
    print('this line of code will also be executed')
another_example_function()