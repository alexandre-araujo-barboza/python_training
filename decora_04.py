from datetime import datetime


def factory_errors(func):
  '''Log the date and time of a function'''

  def handler(number, description, level):
    print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'{"-"*30}')

    return func(number, description, level)
  
  return handler


@factory_errors
def set_error(number, description, level):

  print('Daily backup job has finished.')   
  return "error: " + str(number), description, level

errors= {
    'error_400' : lambda: set_error(400, 'Bad Request ',  'Client Error'),
    'error_500' : lambda: set_error(500, 'Internal Server Error', 'Server Error'),
  }


command = errors['error_400']

# verbose
print(command())

command = errors['error_500']

# silent
command()
