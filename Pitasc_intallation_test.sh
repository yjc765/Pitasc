#!/bin/bash
cd ~./pitasc
tar xf pitasc_2_5_0.tar.gz
tar xf pitasc_common.tar.gz   # extract zip file 'pitasc_2_5_0.tar.gz' and get folder 'install' and pitasc_common

sudo apt install python-catkin-tools 

cd ~/pitasc
rosdep install --from-path install/ -i -y           # install dependencies

source install/setup.bash

terminator -e 'roslaunch pitasc_common bringup_examples.launch' & terminator -e "sleep 5 && rosrun pitasc file_reader.py pitasc_common examples/beginner/simple_move.xml"
