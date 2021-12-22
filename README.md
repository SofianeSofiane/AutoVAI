# AutoVAI
A convolutional neural network-based design of defect detection system. The main purpose of this work was the realization of a prototype of an automated defects detection system in production.
  
The  system is composed of three main subsystems, first the electronic subsystem 
which control the robotic arm and the conveyor belt including motors and sensors, secondly a mechanical 
subsystem which include the conveyor belt, robotic arm and the frame, finally the software subsystem which is 
the important part in the system which is a smart system that performs through quality checks down to the fines details. 
![autovi](https://user-images.githubusercontent.com/96339267/147107034-37a1f75f-bbcc-4c38-a373-32ab7f2dce6a.jpg)

## Mechanical Subsystem
- the pieces of the robotic arm are made with a 3D printer  and Solidworks, the robotic arm composed from 5 axis using 
servo motors in each axe.
- The conveyor belt helped us to move the product to the inspection point, we've used a 
stepper motor to move the conveyor belt, because the stepper motor can move with a precise step.


## Electronic Subsystem
- We've use two microcontrollers to command the systeme, PIC12 & PIC16
- The microcontrollers was programmed with embedded c language programing using Mikroc pro compiler. 
- The electronic boards were designed and simulated using the ISIS software from PROTEUS. Similarly, the automatic routing for the realization of the printed circuit boards was done using the EasyEDA software.

![j](https://user-images.githubusercontent.com/96339267/147109482-2345fa03-773b-4b24-bfaf-0149ed0e59f3.png)

## Software Subsystem
In this part we've combined between machine vision and deep learning to build a smart system that performs through quality checks down to the fines details. 

- We've used transfer learning to get the best results
- All the programming and model training was done in google colab palteform
- The dataset was built from scratch using data augmentation (https://drive.google.com/drive/folders/1Rhvm25AZc2vGegAZm7xYZKFo-NpyWSjI?usp=sharing)
  - The dataset contain
    - 572 good images
    - 572 defected images

![j](https://user-images.githubusercontent.com/96339267/147110633-dbc6d72a-755a-4bf1-8a2f-64a4d0471bc3.png)

## Software used
- Pycharm
- MATLAB
- Solidworks
- ISIS Proteuse
- Mikro c
- EasyEDA

## Demo
- You find can find the project demo in my linkedin page here: www.linkedin.com/in/sofianeabouchi19
## Credit
The work was done with the help of:
- Dr.Skander benseguni
- Mr.Mohammed Belayati


