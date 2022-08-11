import pymunk as pm
import pygame as pg
from multiprocessing import Process
from world import World



class prop(pm.Poly,Process):
    def __init__(self,x,y, world ,moment = 10000):
        self.world = world
        super().__init__(pm.Body(self.world.mass,moment),[(-self.world.r,-self.world.r), (self.world.r,-self.world.r), (self.world.r,self.world.r), (-self.world.r,self.world.r)])
        self.body.position = x,y
        self.rad = self.world.r

        self.ground = False

    

    def check_ground(self, world):
        if self.body.position_y >= (world.ground_y-self.rad):
            self.ground = True
        else:
            self.ground = False

class prop_free(prop,Process):
        def __init__(self,x,y, world):
            super().__init__(x,y, world)
            self.friction = 10
            self.collision_type = 0  

                    