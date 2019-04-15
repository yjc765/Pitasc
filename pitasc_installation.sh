#!/bin/bash
cd ~./pitasc
tar xf pitasc_2_5_0.tar.gz
tar xf pitasc_common.tar.gz   # extract zip file 'pitasc_2_5_0.tar.gz' and get folder 'install' and pitasc_common

sudo apt install python-catkin-tools 

cd ~/pitasc
rosdep install --from-path install/ -i -y           # install dependencies

source install/setup.bash

terminator -e 'roslaunch pitasc_common bringup_examples.launch' & terminator -e "sleep 5 && rosrun pitasc file_reader.py pitasc_common examples/beginner/simple_move.xml"


##########################
# remove files used/created by catkin_make, in your own workspace 

$ cd ~/catkin_ws
$ rm .catkin_workspace
$ rm src/CMakeLists.txt
$ rm -rf build/ devel/ install/

# $ source /opt/ros/kinetic/setup.bash                  # automatically done by sourcing the /pitasc/setup.dash
$ source ~/pitasc/install/setup.bash  

$ catkin init
$ catkin build

# move the extracted pitasc_commom.tar.gz folder to catkin_ws/src

$ source ~/catkin_ws/devel/setup.bash
$ roslaunch pitasc_common bringup_examples.launch 

# in a new terminal
$ source ~/catkin_ws/devel/setup.bash
$ rosrun pitasc file_reader.py pitasc_common examples/beginner/simple_move.xml
