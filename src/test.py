import sys, time #, explorerhat
from curtsies import Input
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow
from math import ceil

class Robot:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.active = bool(left_motor) and bool(right_motor)
        self.power_left = 0
        self.power_right = 0

    def forward(self):
        print(green('forward'))
        if self.power_left < 1: self.power_left += 1
        if self.power_right < 1: self.power_right += 1

        self.move()

    def backward(self):
        print(green('backward'))
        if self.power_left > -1: self.power_left -= 1
        if self.power_right > -1: self.power_right -= 1

        self.move()

    def left(self):
        print(green('left'))
        if self.power_left > -1: self.power_left -= 1
        if self.power_right < 1: self.power_right += 1

        self.move()

    def right(self):
        print(green('right'))
        if self.power_left < 1: self.power_left += 1
        if self.power_right > -1: self.power_right -= 1

        self.move()

    def move(self):
        print(yellow("left: " + str(self.power_left) + " right: " + str(self.power_right)))
        left_base = 100
        right_base = 17

        if self.active:
            if self.power_left > 0:
                self.left_motor.forward(left_base)
            elif self.power_left < 0:
                self.left_motor.backward(left_base)
            else:
                self.left_motor.stop()

            if self.power_right > 0:
                self.right_motor.forward(right_base)
            elif self.power_right < 0:
                self.right_motor.backward(right_base)
            else:
                self.right_motor.stop()

    def stop(self):
        print(green('stop'))
        self.power_left = 0
        self.power_right = 0

        self.move()

# robot = Robot(explorerhat.motor.one, explorerhat.motor.two)
robot = Robot(None, None)

print(yellow('use UP, DOWN, LEFT & RIGHT to steer - SPACE to stop'))
with Input() as input_generator:
    for c in input_generator:
        if c == '<ESC>':
            break
        elif c == '<SPACE>' or c == '<Ctrl-j>':
            robot.stop()
        elif c == '<UP>':
            robot.forward()
        elif c == '<DOWN>':
            robot.backward()
        elif c == '<LEFT>':
            robot.left()
        elif c == '<RIGHT>':
            robot.right()
        else:
            print(yellow(c))
