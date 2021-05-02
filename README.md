# Goal of this project

- real-time object detection with YOLOv3 or tiny yolo

## raspberry pi 4 setup command

- 가상환경
  - python3 -m venv --system-site-packages ./venv
- 가상환경 시작
  - source ./venv/bin/activate

## install command

$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
$ sudo apt-get install libatlas-base-dev libatlas3-base
$ sudo pip3 install h5py==2.10.0
$ sudo pip3 install -U --user six wheel mock
$ wget https://github.com/Qengineering/Tensorflow-Raspberry-Pi/raw/master/tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
$ sudo -H pip3 install tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
$ sudo reboot
