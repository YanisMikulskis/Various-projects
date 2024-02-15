import pygame as pg
import pymunk
import sys
from window_size_snake_sand import size_window

class PLATFORM():
    def __init__(self,cl_space, LX, LY, RX, RY, size):
        self.cl_space = cl_space
        self.LX, self.LY, self.RX, self.RY = LX,LY,RX,RY
        self.platform = pymunk.Segment(self.cl_space.static_body, (self.LX, self.LY), (self.RX, self.RY), size)
        self.platform.elasticity = 0.8
        self.platform.friction = 1.0
    def location(self):
        self.cl_space.add(self.platform)
    def options(self, arg_fps, arg_draw_options): #метод для цикла окна
        self.cl_space.step(1/arg_fps)
        self.cl_space.debug_draw(arg_draw_options)