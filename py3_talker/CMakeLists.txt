cmake_minimum_required(VERSION 2.8.3)
project(py3_talker)

find_package(catkin REQUIRED
    rospy
    std_msgs
)

catkin_python_setup()

catkin_package()

###########
## Build ##
###########

include_directories()

############
# Install ##
############

catkin_install_python(PROGRAMS nodes/talker_node.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})