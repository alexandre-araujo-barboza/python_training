# Decorador com log de erros
import logging, time, os

def factory_decorator(log):
  logging.basicConfig(filename=log, level=logging.ERROR)
  print('Decorator called...')

  def factory_function(function):
    print('\tfunction called...')

    def nested_function(*args, **kwargs):
      print('\t\tNested...')
      print('\t\tDecorator params:', log)
      
      result = function(*args, **kwargs)
      print('\t\t\tArgs:', args)
      return result
    
    return nested_function
  
  return factory_function

def factory_errors(error, message, type):
  d = time.strftime("%Y-%m-%d", time.localtime())
  t = time.strftime("%H:%M:%S", time.localtime())
  try:
    raise Exception(error, message, type, d, t)
  except Exception as inst:
    return inst

set_error_400 = factory_errors(400, 'Bad Request ',  'Client Error')
set_error_401 = factory_errors(401, 'Unauthorized',  'Client Error')
set_error_402 = factory_errors(402, 'Payment Required',  'Client Error')
set_error_403 = factory_errors(403, 'Forbidden',  'Client Error')
set_error_404 = factory_errors(404, 'Not Found',  'Client Error')
set_error_405 = factory_errors(405, 'Method Not Allowed',  'Client Error')
set_error_406 = factory_errors(406, 'Not Acceptable',  'Client Error')
set_error_407 = factory_errors(407, 'Proxy Authentication Required',  'Client Error')
set_error_408 = factory_errors(408, 'Request Timeout',  'Client Error')
set_error_409 = factory_errors(409, 'Conflict',  'Client Error')
set_error_410 = factory_errors(410, 'Gone',  'Client Error')
set_error_411 = factory_errors(411, 'Length Required',  'Client Error')
set_error_412 = factory_errors(412, 'Precondition Failed',  'Client Error')
set_error_413 = factory_errors(413, 'Content Too Large',  'Client Error')
set_error_414 = factory_errors(414, 'URI Too Long',  'Client Error')
set_error_415 = factory_errors(415, 'Unsupported Media Type',  'Client Error')
set_error_416 = factory_errors(416, 'Range Not Satisfiable',  'Client Error')
set_error_417 = factory_errors(417, 'Expectation Failed',  'Client Error')
set_error_421 = factory_errors(421, 'Misdirected Request',  'Client Error')
set_error_422 = factory_errors(422, 'Unprocessable Content',  'Client Error')
set_error_423 = factory_errors(423, 'Locked',  'Client Error')
set_error_424 = factory_errors(424, 'Failed Dependency',  'Client Error')
set_error_425 = factory_errors(425, 'Too Early',  'Client Error')
set_error_426 = factory_errors(426, 'Upgrade Required',  'Client Error')
set_error_428 = factory_errors(428, 'Precondition Required',  'Client Error')
set_error_429 = factory_errors(429, 'Too Many Requests',  'Client Error')
set_error_431 = factory_errors(431, 'Request Header Fields Too Large',  'Client Error')
set_error_451 = factory_errors(451, 'Unavailable for Legal Reasons',  'Client Error')

set_error_500 = factory_errors(500, 'Internal Server Error', 'Server Error')
set_error_501 = factory_errors(501, 'Not Implemented', 'Server Error')
set_error_502 = factory_errors(502, 'Bad Gateway', 'Server Error')
set_error_503 = factory_errors(503, 'Service Unavailable', 'Server Error')
set_error_504 = factory_errors(504, 'Gateway Timeout', 'Server Error')
set_error_505 = factory_errors(505, 'HTTP Version Not Supported', 'Server Error')
set_error_506 = factory_errors(506, 'Variant Also Negotiates', 'Server Error')
set_error_507 = factory_errors(507, 'Insufficient Storage', 'Server Error')
set_error_508 = factory_errors(508, 'Loop Detected', 'Server Error')
set_error_511 = factory_errors(511, 'Network Authentication Required', 'Server Error')

decorator = factory_decorator('error.log')
username  = decorator(lambda login, pid, cwd: (login, pid, cwd))

id = username(os.getlogin(), os.getpid(), os.getcwd())

logging.error(id)
logging.error(set_error_505)
logging.error(set_error_411)
logging.error(set_error_508)

logging.shutdown()
