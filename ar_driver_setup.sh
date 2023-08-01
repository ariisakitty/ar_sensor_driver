#! /bin/bash

# 1. arena_setup.sh
sudo sh setup_script/arena_setup.sh

# 2. fixposition_setup.sh
sudo sh setup_script/fixposition_setup.sh

# 3. hesai_setup.sh
sudo sh setup_script/hesai_setup.sh

# 4. rosdep
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro humble -r -y
