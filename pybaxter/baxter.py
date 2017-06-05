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
 
        self._baxter_state = RobotEnable()

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

    @property
    def enabled(self):
        return self._baxter_state.state().enabled
    @property
    def left_s0(self):
        return self._limbs[LEFT].joint_angles()['left_s0']
    @property
    def left_s1(self):
        return self._limbs[LEFT].joint_angles()['left_s1']
    @property
    def left_e0(self):
        return self._limbs[LEFT].joint_angles()['left_e0']
    @property
    def left_e1(self):
        return self._limbs[LEFT].joint_angles()['left_e1']
    @property
    def left_w0(self):
        return self._limbs[LEFT].joint_angles()['left_w0']
    @property
    def left_w1(self):
        return self._limbs[LEFT].joint_angles()['left_w1']
    @property
    def left_w2(self):
        return self._limbs[LEFT].joint_angles()['left_w2']
    @property
    def right_s0(self):
        return self._limbs[RIGHT].joint_angles()['right_s0']
    @property
    def right_s1(self):
        return self._limbs[RIGHT].joint_angles()['right_s1']
    @property
    def right_e0(self):
        return self._limbs[RIGHT].joint_angles()['right_e0']
    @property
    def right_e1(self):
        return self._limbs[RIGHT].joint_angles()['right_e1']
    @property
    def right_w0(self):
        return self._limbs[RIGHT].joint_angles()['right_w0']
    @property
    def right_w1(self):
        return self._limbs[RIGHT].joint_angles()['right_w0']
    @property
    def right_w2(self):
        return self._limbs[RIGHT].joint_angles()['right_w0']
