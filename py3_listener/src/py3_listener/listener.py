#!/usr/bin/env python3

'''
@file     listener.py
@package  py3_listner
@author   CVH95
@email    cvh95@todo.com
@brief    Fibonacci listener

Copyright (C) 2021 MIT License
'''

import rospy
from std_msgs.msg import *


class Listener:
    def __init__(self):

        self.fibonacci = 0
        self.subscriber = rospy.Subscriber(
            'innosold/process/layer', Int64, self.callback)
        rospy.on_shutdown(self.close)

    def callback(self, msg):

        self.fibonacci = msg.data
        rospy.loginfo('Fibonacci value: %d' % self.fibonacci)

    def close(self):
        print('\nLast value received: %d' % self.fibonacci)
