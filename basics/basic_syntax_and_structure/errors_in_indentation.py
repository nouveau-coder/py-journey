#being a crucial part of python's syntax, incorrect indentation will lead to a SyntaxError.
'''
if True:
print('this line is not indented, giving a error')
'''
#the line above will give an IndentationError because the print statement is not indented. the simple fix is to indent the line.
if True:
    print('this line is indented correctly')