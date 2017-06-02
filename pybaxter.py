#!/usr/bin/env python2

from baxter_interface import Limb, RobotEnable
from rospy import init_node
from sys import exit

class Baxter(object):
    def __init__(self, name='Baxter_Node'):
	self._name = name
	init_node(self._name)
	RobotEnable().enable()
	self._limbs = {
	    'left': Limb('left'),
            'right': Limb('right')
        }

    def reset_limb(self, side):
        angles = {joint: 0.0 for joint in self._limbs[side].joint_angles()}
	self._limbs[side].move_to_joint_positions(angles)

    def joints(self):
        joints = {
            'left': self._limbs['left'].joint_angles(),
            'right': self._limbs['right'].joint_angles()
        }
        return joints

if __name__ == '__main__':
    node = Baxter()
    node.reset_limb('left')
    node.reset_limb('right')
    print(node.joints())
    exit()
