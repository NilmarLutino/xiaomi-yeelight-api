import sys
sys.path.append('../')

from yeelight import SmartBulb

bulb = SmartBulb('192.168.0.102')

print('Name: %s' % bulb.name)