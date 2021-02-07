#!/usr/bin/env python3

'''
@file     listener_node.py
@package  py3_listner
@author   CVH95
@email    cvh95@todo.com
@brief    Fibonacci listener

Copyright (C) 2021 MIT License
'''

import sys
import rospy
from py3_listener.listener import Listener

if __name__ == '__main__':
    rospy.init_node('fibonacci_listener', anonymous=True)
    LT = Listener()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
        # print("\n\n\n\n\n\TALKER NODE INTERRUPTED!! \n\nShutting down...\n\n\n\n\n\n")
