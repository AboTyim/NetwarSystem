import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

#handler = logging.handlers.SysLogHandler(address = '/dev/log')
handler = logging.handlers.SysLogHandler(address=('192.168.88.193', 514), facility=logging.handlers.SysLogHandler.LOG_DAEMON)

my_logger.addHandler(handler)

my_logger.debug('this is debug')
my_logger.critical('this is critical')
