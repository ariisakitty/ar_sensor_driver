#! /bin/bash

 sudo apt update
 sudo apt install -y wget
 wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
 sudo apt-get update
 sudo apt install -y build-essential cmake
 sudo apt install -y libeigen3-dev
 sudo apt install -y libyaml-cpp-dev
