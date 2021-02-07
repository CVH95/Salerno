#!/usr/bin/env python3

'''
@file     talker.py
@package  py3_talker
@author   CVH95
@email    cvh95@todo.com
@brief    Fibonacci publisher

Copyright (C) 2021 MIT License
'''

import rospy
from std_msgs.msg import *


class Talker:
    def __init__(self):

        self.current = 1
        self.previous = 0

        self.publisher = rospy.Publisher(
            'innosold/process/layer', Int64, queue_size=1)
        rospy.on_shutdown(self.close)

    def fibonacci(self):

        try:
            while not rospy.is_shutdown():
                next_in_series = self.previous + self.current

                msg = Int64()
                msg.data = next_in_series
                self.publisher.publish(msg)

                self.previous = self.current
                self.current = next_in_series

                rospy.sleep(0.5)
        except rospy.ROSInterruptException:
            self.close()

    def close(self):
        print('\nFinished Fibonacci series with %d, %d' %
              (self.previous, self.current))
