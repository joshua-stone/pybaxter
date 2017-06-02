#!/usr/bin/env python2

from baxter_interface import Limb, RobotEnable
from rospy import init_node
from sys import exit

class Baxter(object):
    _arm_joints = {
        'left': [
            'left_s0',
            'left_s1',
            'left_e0',
            'left_e1',
            'left_w0',
            'left_w1',
            'left_w2'
        ],
        'right': [
            'right_s0',
            'right_s1',
            'right_e0',
            'right_e1',
            'right_w0',
            'right_w1',
            'right_w2'
        ]
    }
    def __init__(self, name='Baxter_Node'):
	self._name = name
	init_node(self._name)
	RobotEnable().enable()
	self._limbs = {
	    'left': Limb('left'),
            'right': Limb('right')
        }
		 
    def set_angles_to_zero(self, side):
        angles = {joint: 0.0 for joint in self._arm_joints[side]}
	self._limbs[side].move_to_joint_positions(angles)

node = Baxter()
node.set_angles_to_zero('right')

exit	
