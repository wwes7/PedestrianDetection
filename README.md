# PedestrianDetection
## Designed by Huanqi Yang in UESTC, 5/2018
### Introduction 
In this project, I use two ways to realize pedestrian dectection in a video provided by professor Lian Yan, UESTC. 
#### 1.transfer video into split pictures, and recognize and mark pedestrian on the pictures, then joint all the pictures.
#### 2.read video frame by frame, and show direct the marked video frame by frame.
### 1.details about the first way
1)you can use file:[extract pic.py] to tranfer the video into pictures frame by frame.
2)use file[strengthenpic.py] to process the pictures for better results.(optional)
3)use file[detcet.py] to recognize pedestrain in all the pictures.
4)use file[trans to vid] to joint all the recognized pictures into a video.
### 2.details about the second way
run file[recg_realtime.py], which can show the result video directly.
### 3.intro:file:[split_images]
the after tranfering images of the video:./video/person.mkv, which was shot by a camera in a driving car.
examples:
![example1](split_images/images100000000000.png)
![example1](split_images/images69800000000000.png)
![example1](split_images/images82900000000000.png)
### 4.intro:file:[reg_split_images]
the recognized images
examples:
![example1](reg_split_images/images00000008.png)
![example1](reg_split_images/images00000171.png)
![example1](reg_split_images/images00000191.png)
