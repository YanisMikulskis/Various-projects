import pygame as pg
import pymunk
import sys
from window_size_snake_sand import size_window
import random as rnd
class SAND():
    def __init__(self, cl_space, mass, rad, posit):
        self.space = cl_space
        self.mass = mass
        self.rad = rad
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.rad)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = posit
        self.ball = pymunk.Circle(self.body, self.rad)
        self.ball.color = [rnd.randint(1, 255) for i in range(4)]
    def location(self):
        self.space.add(self.body, self.ball)
