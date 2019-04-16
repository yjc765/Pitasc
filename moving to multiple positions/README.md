The file 'moving_pubisher' publishes the messages to move the target1 in a loop, the 'moving_sublisher' subscribes the location message of Publisher. 

How to run them?
1. move these two files to `~/catkin_ws/src/pitasc_common/scripts`
2. make them executable   
   `$ chmod +x ~/catkin_ws/src/pitasc_common/scripts/moving_publisher.py`\
   `$ chmod +x ~/catkin_ws/src/pitasc_common/scripts/moving_subscriber.py`   
3. Open your GUI by
   `$ roslaunch pitasc_common bringup_examples.launch`
4. run your files\
   `$ rosrun pitasc_common moving_publisher.py`\
   `$ rosrun pitasc_common moving_subscriber.py`
5. move `track_frame.xml` to `catkin_ws/src/pitasc_common/examples/beginner`
   run `track_frame.xml` file to visualize how robotor tracks the target1.
   `$ rosrun pitasc file_reader.py pitasc_common examples/beginner/track_frame.xml`
