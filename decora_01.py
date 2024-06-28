# Decoradores com parâmetros

def factory_decorator(a=None, b=None, c=None):
  def factory_function(function):
    print('Decorator called...')

    def nested_function(*args, **kwargs):
      print('Decorator params: ', a, b, c)
      print('Nested...')
      
      result = function(*args, **kwargs)
      return result
    
    return nested_function
  return factory_function

@factory_decorator('a', 'b', 'c')
def sum(x, y):
    return x + y

decorator = factory_decorator()
multiplicator = decorator(lambda x, y: x * y)

ten_plus_five = sum(10, 5)
ten_multiply_five = multiplicator(10, 5)

print('10 + 5 = ', ten_plus_five)
print('10 x 5 = ', ten_multiply_five)
