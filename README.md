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
$ sudo apt-get install libgtk2.0-dev
$ pip3 install opencv-python
$ pip3 install opencv-contrib-python
$ pip3 install -U numpy
$ wget https://github.com/Qengineering/Tensorflow-Raspberry-Pi/raw/master/tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
$ sudo -H pip3 install tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
$ sudo reboot

## 에러

- no module named yolo3 ~~ : python 상대경로 import 문제입니다.
  - sys.path.append('~경로경로경로') 를 import 하기 전에 넣어줍니다.

## 문제

- 라즈베리파이4 8gb 이용중임에도 속도가 조금 느림을 확인
  - cv2.imshow() 로 보여주는 속도가 매우 느리고 yolo자체는 속도가 그렇게까지 느리지는 않은듯함
    - 원인으로는 아래와 같은것이 예상됩니다.
    - detect_image 함수를 쓰려고 PIL 로 바꾸는 과정이 추가되기때문에 성능저하
    - vnc 사용
    <!-- TODO : tiny yolo 도 한번 시도해보고 속도가 느리면 내부함수 수정? -->
