# TeamFortress2-YoloV5

Fair AI's in games is a big problem in the games industry. On the one hand, the Pc-controlled opponents are too difficult because they can read all information directly, or on the other hand, the artificial opponent is deliberately set to be too 'stupid' so that it no longer presents a challenge. So the only option is to first programme a perfect opponent AI and then let it gradually make mistakes or slow down.

A new approach would be to design or use a neural network that only sees what a human player sees. At least in theory, this AI sounds fairer this way, since either a state transition system or another neural network could be used as a controller to take over the control and reaction.

For this, the application 'Team Fortress 2' is used as an example, since it has non-trivial problems in several criteria. Images (videos) are used as input to the network and the output should be whether and which units are on the image seen, as well as their quantity.

# Data source
The model was trained with 6700 labled pictures. The best results can be achieved with the standard models of tf2-characters.

# Models

## My custom network
![This is an image](https://github.com/poetter-sebastian/TeamFortress2-YoloV5/blob/main/img/test_custom.jpg)

## YoloV5 S
![This is an image](https://github.com/poetter-sebastian/TeamFortress2-YoloV5/blob/main/img/test_s.jpg)

## YoloV5 M
![This is an image](https://github.com/poetter-sebastian/TeamFortress2-YoloV5/blob/main/img/test_m.jpg)

## YoloV5 L
![This is an image](https://github.com/poetter-sebastian/TeamFortress2-YoloV5/blob/main/img/test_l.jpg)

## YoloV5 X (best model)
![This is an image](https://github.com/poetter-sebastian/TeamFortress2-YoloV5/blob/main/img/test_x.jpg)
