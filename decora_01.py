# Decoradores com parâmetros

def decorator_factory(a=None, b=None, c=None):
  def function_factory(function):
    print('Decorator called...')

    def nested_function(*args, **kwargs):
      print('Decorator params: ', a, b, c)
      print('Nested...')
      
      result = function(*args, **kwargs)
      return result
    
    return nested_function
  
  return function_factory

@decorator_factory('a', 'b', 'c')
def sum(x, y):
    return x + y

decorator = decorator_factory()
multiplicator = decorator(lambda x, y: x * y)

ten_plus_five = sum(10, 5)
ten_multiply_five = multiplicator(10, 5)

print('10 + 5 = ', ten_plus_five)
print('10 x 5 = ', ten_multiply_five)
