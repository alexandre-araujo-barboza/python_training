from datetime import datetime
import logging, os

def factory_errors(func):
  def handler(number, description, level):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    os_user = os.getlogin()
    os_pid  = os.getpid()
    os_cwd  = os.getcwd()
    logging.error((
      timestamp,
      number,
      description,
      level,
      os_user,
      os_pid,
      os_cwd
    ))    
    logging.shutdown()
    return func(number, description, level)
  return handler

@factory_errors
def set_error(number, description, level):
  try:
    raise Exception ('Sorry, an error occurred: ' + str(number) + ' - ' + description + ' (' + level + ').\nPlease, see the error log for details.')
  except Exception as inst:
    return inst
  
errors= {
    'error_400' : lambda: set_error(400, 'Bad Request ',  'Client Error'),
    'error_401' : lambda: set_error(401, 'Unauthorized',  'Client Error'),
    'error_402' : lambda: set_error(402, 'Payment Required',  'Client Error'),
    'error_403' : lambda: set_error(403, 'Forbidden',  'Client Error'),
    'error_404' : lambda: set_error(404, 'Not Found',  'Client Error'),
    'error_405' : lambda: set_error(405, 'Method Not Allowed',  'Client Error'),
    'error_406' : lambda: set_error(406, 'Not Acceptable',  'Client Error'),
    'error_407' : lambda: set_error(407, 'Proxy Authentication Required',  'Client Error'),
    'error_408' : lambda: set_error(408, 'Request Timeout',  'Client Error'),
    'error_409' : lambda: set_error(409, 'Conflict',  'Client Error'),
    'error_410' : lambda: set_error(410, 'Gone',  'Client Error'),
    'error_411' : lambda: set_error(411, 'Length Required',  'Client Error'),
    'error_412' : lambda: set_error(412, 'Precondition Failed',  'Client Error'),
    'error_413' : lambda: set_error(413, 'Content Too Large',  'Client Error'),
    'error_414' : lambda: set_error(414, 'URI Too Long',  'Client Error'),
    'error_415' : lambda: set_error(415, 'Unsupported Media Type',  'Client Error'),
    'error_416' : lambda: set_error(416, 'Range Not Satisfiable',  'Client Error'),
    'error_417' : lambda: set_error(417, 'Expectation Failed',  'Client Error'),
    'error_421' : lambda: set_error(421, 'Misdirected Request',  'Client Error'),
    'error_422' : lambda: set_error(422, 'Unprocessable Content',  'Client Error'),
    'error_423' : lambda: set_error(423, 'Locked',  'Client Error'),
    'error_424' : lambda: set_error(424, 'Failed Dependency',  'Client Error'),
    'error_425' : lambda: set_error(425, 'Too Early',  'Client Error'),
    'error_426' : lambda: set_error(426, 'Upgrade Required',  'Client Error'),
    'error_428' : lambda: set_error(428, 'Precondition Required',  'Client Error'),
    'error_429' : lambda: set_error(429, 'Too Many Requests',  'Client Error'),
    'error_431' : lambda: set_error(431, 'Request Header Fields Too Large',  'Client Error'),
    'error_451' : lambda: set_error(451, 'Unavailable for Legal Reasons',  'Client Error'),
    'error_500' : lambda: set_error(500, 'Internal Server Error', 'Server Error'),
    'error_501' : lambda: set_error(501, 'Not Implemented', 'Server Error'),
    'error_502' : lambda: set_error(502, 'Bad Gateway', 'Server Error'),
    'error_503' : lambda: set_error(503, 'Service Unavailable', 'Server Error'),
    'error_504' : lambda: set_error(504, 'Gateway Timeout', 'Server Error'),
    'error_505' : lambda: set_error(505, 'HTTP Version Not Supported', 'Server Error'),
    'error_506' : lambda: set_error(506, 'Variant Also Negotiates', 'Server Error'),
    'error_507' : lambda: set_error(507, 'Insufficient Storage', 'Server Error'),
    'error_508' : lambda: set_error(508, 'Loop Detected', 'Server Error'),
    'error_511' : lambda: set_error(511, 'Network Authentication Required', 'Server Error'),
  }

command = errors['error_400']
# Do something risky to client
...

# if an error occurs
# verbose
print(command())

command = errors['error_500']
# Do something risky to server
...

# if an error occurs
# silent
command()
