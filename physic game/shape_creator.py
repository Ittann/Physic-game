from turtle import position, width
import pymunk as pm
from props import prop_free
from multiprocessing import Process
class ShapeCreator(Process):
    def __init__(self, world, space):

            self.world = world
            self.space = space


    def create_free_prop(self,x,y):
        if self.world.Poly == True:
            free_prop = prop_free(x,y, self.world)
            free_prop.elasticity = 0.1
            free_prop.friction = 1.0
            self.space.add(free_prop, free_prop.body) 
            self.world.free_props.append(free_prop)

        if self.world.Circle == True:
            self.ball_moment = pm.moment_for_circle(self.world.ball_mass, 0, self.world.ball_rad)
            ball_body = pm.Body(self.world.ball_mass, self.ball_moment)
            ball_body.position = x,y
            shape = pm.Circle(ball_body, self.world.ball_rad )
            shape.elasticity = 0.8
            shape.friction = 0.5
            self.space.add(ball_body, shape)
            self.world.free_props.append(shape)

        if self.world.Line == True:
            self.line_moment = pm.moment_for_segment(self.world.line_mass, [0,0], [self.world.line_dli,self.world.line_dli], self.world.line_rad)
            line_body = pm.Body(self.world.line_mass, self.line_moment)
            line_body.position = x,y
            line_body.center_of_gravity = (self.world.line_dli/2,self.world.line_dli/2)
            shape = pm.Segment(line_body, (-1,-1), (self.world.line_dli,self.world.line_dli), self.world.line_rad)
            shape.elasticity = 0.6
            shape.friction = 0.4
            self.space.add(line_body, shape)
            self.world.free_props.append(shape)


    def remove_noclipped_props(self):
        for prop in self.world.free_props:
            if prop.body.position.x < -50 or prop.body.position.x > self.world.width + 50:
                self.world.free_props.remove(prop)
                self.space.remove(prop.body, prop)
                #print("noclipped") #"- done, all work" 
            elif prop.body.position.y > self.world.height:
                self.world.free_props.remove(prop)
                self.space.remove(prop.body, prop)
                #print("noclipped") #- done, all work    
    def remove_all_props(self):
        self.world.shape_being_dragged = None

        for free_prop in self.world.free_props:
            self.space.remove(free_prop)

        self.world.free_props.clear()

    def create_static_floor(self, height = 15, friction = 10):
         
        body = pm.Body(body_type= pm.Body.STATIC)
        body.position = [self.world.width/2, self.world.ground_y]
        semiwidth = self.world.width/2
        vs = [(-semiwidth, 0), (semiwidth, 0), (-semiwidth, height), (semiwidth, height)]

        poly = pm.Poly(body,vs)

        poly.friction = friction
        poly.collision_type = 2
        poly.elasticity = 0.4
        self.space.add(body, poly)



    def create_static_wall(self,x,y,height=1,friction=100):

        body = pm.Body(body_type= pm.Body.STATIC)
        body.position = [x,y]
        line = pm.Segment(body, (0,0), (0, -self.world.height), width)
        line.friction = friction
        line.collision_type = 3
        line.space.add(body, line)