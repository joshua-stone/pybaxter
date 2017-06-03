#!/usr/bin/env python2

from baxter_interface import Limb, RobotEnable
from rospy import init_node

__all__ = [
    'Baxter',
    'LEFT',
    'RIGHT'
]

LEFT, RIGHT = 'left', 'right'

class Baxter(object):
    def __init__(self, name='Baxter_Node'):
	self._name = name
	init_node(self._name)
	RobotEnable().enable()
	self._limbs = {
	    LEFT: Limb(LEFT),
            RIGHT: Limb(RIGHT)
        }

    def reset_limb(self, side):
        angles = {joint: 0.0 for joint in self._limbs[side].joint_angles()}
	self._limbs[side].move_to_joint_positions(angles)

    def joints(self):
        joints = {limb: joint.joint_angles() for limb, joint in self._limbs.iteritems()}
        return joints

