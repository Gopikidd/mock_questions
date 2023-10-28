# https://docs.python.org/3/library/exceptions.html
''''''
'''
Exception: Can be handled : try, except  blocks
Error    : Cant be handled : 
                  : Memory Errors 
                  : System exits


BaseException
 +-- Exception***          (Polygon)
      +-- ArithmeticError *       Quadrilateral
      |    +-- FloatingPointError       Square
      |    +-- OverflowError
      |    +-- ZeroDivisionError *
      +-- AssertionError *
      +-- ImportError
      |    +-- ModuleNotFoundError *
      +-- LookupError
      |    +-- IndexError *
      |    +-- KeyError *
      +-- NameError *
      |    +-- UnboundLocalError
      +-- OSError *
      +-- RuntimeError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError *
      +-- ValueError *
           '''
print("Type error example")
print("Additions: ", 10 + 'Madhu')   # TypeError Exception
print("ZDE example")
# print("Division : ", 10/0)
