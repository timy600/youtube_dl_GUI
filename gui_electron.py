# https://medium.com/@abulka/electron-python-4e8c807bfa5e

# https://github.com/fyears/electron-python-example

import zerorpc
import gevent, signalport = 1234
addr = 'tcp://127.0.0.1:' + port
s = zerorpc.Server(PythermalApi())
s.bind(addr)gevent.signal(signal.SIGTERM, s.stop)
gevent.signal(signal.SIGINT, s.stop)  # ^C

s.run()



# and now we can call on Python:
# Python code
class PythermalApi(object):    def echo(self, text):
    """echo any text"""
    return text    
#.... (more endpoints) ...
