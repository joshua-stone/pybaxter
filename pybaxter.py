#!/usr/bin/env python2

from baxter_interface import Limb, RobotEnable
from rospy import init_node
from sys import exit

class Baxter(object):
    def __init__(self, name='Baxter_Node'):
	self._name = name
	init_node(self._name)
	RobotEnable().enable()
 
    def set_angles_to_zero(self, side):
	limb = Limb(side)
        angles = {'{}_{}'.format(side, location): 0.0 for location in ('s0', 's1', 'e0', 'e1', 'w0', 'w1', 'w2')}
	limb.move_to_joint_positions(angles)

node = Baxter()
node.set_angles_to_zero('left')

exit	
