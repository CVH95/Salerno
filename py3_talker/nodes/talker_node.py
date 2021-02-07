#!/usr/bin/env python3

'''
@file     talker_node.py
@package  py3_talker
@author   CVH95
@email    cvh95@todo.com
@brief    Fibonacci publisher

Copyright (C) 2021 MIT License
'''

import sys
import rospy
from py3_talker.talker import Talker

if __name__ == '__main__':
    rospy.init_node('fibonacci_talker', anonymous=True)
    TK = Talker()
    try:
        TK.fibonacci()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
