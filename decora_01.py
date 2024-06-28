# Decoradores com parâmetros

def factory_decorator(a=None, b=None, c=None):
  print('Decorator called...')

  def factory_function(function):
    print('\tfunction called...')
     
    def nested_function(*args, **kwargs):
      print('\t\tNested...')
      print('\t\tDecorator params:', a, b, c)
      
      result = function(*args, **kwargs)
      return result
    
    return nested_function
  
  return factory_function

@factory_decorator('d', 'e', 'f') # SECOND
@factory_decorator('a', 'b', 'c') # FIRST

def sum(x, y):
    return x + y

decorator = factory_decorator()
multiplicator = decorator(lambda x, y: x * y)

ten_plus_five = sum(10, 5)
ten_multiply_five = multiplicator(10, 5)

print('10 + 5 = ', ten_plus_five)
print('10 x 5 = ', ten_multiply_five)
