# ar_sensor_driver

-----
# ArenaSDK - v0.1.68 as of 7/31/2023

  1) Download Ubuntu 22.04 version from https://thinklucid.com/downloads-hub/

  2) Extract the tarball to your desired location:

    $ tar -xvzf ArenaSDK_Linux.tar.gz
    where ArenaSDK_Linux.tar.gz is the tarball name.

  3) Run the Arena_SDK.conf file

    $ cd /path/to/ArenaSDK_Linux
    $ sudo sh Arena_SDK_Linux_x64.conf
    
    This will make the Arena SDK shared library files accessible by the run-time linker (ld.so or ld-linux.so).

-----
# ar_driver_setup

    $ sh ar_driver_setup.sh
    
-----
# build & install

    $ colcon build --symlink-install
    $ source install/setup.bash (assuming /opt/ros/humble/setup.bash is already done)
    
-----
# launch

  1) Triton
  
    $ ros2 run arena_camera_node start --ros-args -p pixelformat:=rgb8

  2) XVN
  
    $ ros2 launch fixposition_driver_ros2 tcp.launch
    
  3) QT128
  
    $ ros2 launch pandar_pointcloud PandarSwift_points.py

