#!/bin/bash
cd ~/catkin_ws
rm .catkin_workspace
rm src/CMakeLists.txt
rm -rf build/ devel/ install/

# $ source /opt/ros/kinetic/setup.bash                  # automatically done by sourcing the /pitasc/setup.dash
source ~/pitasc/install/setup.bash  

catkin init
catkin build

# move the extracted pitasc_commom.tar.gz folder to catkin_ws/src
mv ~/pitasc/install ~/catkin_ws/src

source ~/catkin_ws/devel/setup.bash

terminator -e 'roslaunch pitasc_common bringup_examples.launch' & terminator -e "sleep 5 && rosrun pitasc file_reader.py pitasc_common examples/beginner/simple_move.xml"
