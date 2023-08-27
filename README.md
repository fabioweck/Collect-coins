# Collect-coins
Game developed with Python!

This simple game is a Pygame practice as part of Python Programming MOOC 2023 from University of Helsinki - Finland.
It was developed under requirements of the course.
The game consists of a robot which has a task to catch a coin located on the opposite screen border.
When the robot tries to follow the path to the coin, it faces enemies (monsters) crossing the screen.
Each monster moves on its pace, defined by random values delivered by "randint" method after instantiation.
Upon crossing the path and reaching the coin, the robot holds the coin and has another task: bringing the coin
back to the opposite screen border and deliver it to the blue door. Every time the player manages to accomplish the task,
the game goes to upper levels, increasing the speed of the robot as well as the enemies.
If any of the monsters touches the robot in the path, it means that the robot was caught and the game ends, giving the option to
restart the game or quit. In the end screen it is also possible to check the level reached.

The code is all based on OOP (object-oriented programming) and makes use of the PyGame module.
Features like collision detection is included in this module, which makes the code easier to develop.

I hope you enjoy my game!

![image](https://github.com/fabioweck/Collect-coins/assets/115494238/5c34ea9d-881e-4bef-a902-b7cf21684207)
