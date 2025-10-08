#sometimes we need to write comments that span multiple lines. In python, we can use triple quotes (''' or """) to create multiline comments.
'''
this is a multiline comment
it can span multiple lines
everything between the triple quotes is ignored by python
this is useful for writing long comments or documentation
'''
print('this line of code will be executed')
#we can also use triple double quotes for multiline comments.
"""
this is another multiline comment
it also spans multiple lines
everything between the triple double quotes is ignored by python
"""
# Technical note: Triple quotes create multi-line strings, not true comments.
# They work for documentation but are processed differently than '#' comments.
# The Python interpreter ignores these strings if they are not assigned to a variable or used in any way.