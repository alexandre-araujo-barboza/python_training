# Decorador com log de erros personalizados

import logging, time, os

def factory_errors(function):
  # print('Decorator called...')
  # print('\tOn function:', function.__name__)
  
  def error_handler(code, description, level):
    # print('\tInner function called...')
    # print('\t\t', code, '\n\t\t', description, '\n\t\t', level)

    logging.basicConfig(filename='error.log', level=logging.ERROR)
    local_date = time.strftime("%Y-%m-%d", time.localtime())
    local_time = time.strftime("%H:%M:%S", time.localtime())
    os_user = os.getlogin()
    os_pid  = os.getpid()
    os_cwd  = os.getcwd()
    logging.error((
      code,
      description,
      level,
      local_date,
      local_time,
      os_user,
      os_pid,
      os_cwd
    ))    
    logging.shutdown()
    
    try:
      raise Exception ('Sorry, an error occurred: ' + str(code) + ' - ' + description + ' (' + level + ')')
    except Exception as inst:
      return inst
    
  return error_handler
  
@factory_errors
def set_error(code, description,  level):
  ...

# verbose mode
print(set_error(300, "Custom Error", "My Error"))

# silent mode
set_error(400, 'Bad Request ',  'Client Error')
set_error(500, 'Internal Server Error', 'Server Error')
