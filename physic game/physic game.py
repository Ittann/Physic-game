from msilib.schema import Font
import pygame as pg
import pymunk as pm
from pymunk import pygame_util
from world import World
from shape_creator import ShapeCreator
from multiprocessing import Process
class Game(Process):
    def __init__(self):
        self.caption = "physic game alpha 0.1"
        self.fps = 60
        pg.display.init()
        self.infoObject = pg.display.Info()
        self.camera_width = 1280
        self.camera_height = 768
        self.fullscreen = True
        #arg for radius, mass and length 
        self.onpol = True
        self.oncircle = False
        self.onlien = False
        #RGB
        self.r = 50
        self.g  = 50
        self.b = 50
        self.r1 = 250
        self.g1 = 50
        self.b1 = 50
        self.r3 = 50
        self.g3 = 50
        self.b3 = 50







    def game_ini(self):
        pg.init()
        camera = pg.display.set_mode((self.camera_width,self.camera_height), pg.FULLSCREEN) 
        pg.display.set_caption(self.caption)
        clock = pg.time.Clock()
        pg.display.set_icon(pg.image.load("pgic.bmp"))

        font = pg.font.SysFont('Courier New', 15)

        fon = pg.font.SysFont('Courier New', 20)
        world = World(self.camera_width, self.camera_height, camera)

        pm.pygame_util.positive_y_is_up = False

        self.game_run(camera, clock, font, world, fon)

    def game_run(self,camera,clock,font,world, fon):


        draw_options = pm.pygame_util.DrawOptions(world)


        space =  pm.Space()
        space.gravity = (0.0, 1000.0)
        space.iterations = 80

        shape_creator = ShapeCreator(world,space)

        shape_creator.create_static_floor()

        shape_creator.create_static_floor(0, world.ground_y)
        shape_creator.create_static_floor(world.width-1, world.ground_y)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if  event.type == pg.KEYDOWN:  
                    if  event.key == pg.K_ESCAPE:
                        quit()
                    if event.key == pg.K_r:
                        shape_creator.remove_all_props()  
                    if event.key ==  pg.K_1:
                        if world.Poly == False:
                            world.Poly = True
                            world.Circle = False
                            world.Line = False
                            if world.Line == False and world.Poly == True and self.onlien == True:
                                self.r = 50
                                self.onlien = False
                                self.r3 = 250
                                self.oncircle = True                

                    if event.key == pg.K_2:
                        if world.Circle == False:
                            world.Circle = True
                            world.Poly = False
                            world.Line = False
                            if world.Line == False and world.Circle == True and self.onlien == True:
                                self.r = 50
                                self.onlien = False
                                self.r3 = 250
                                self.oncircle = True
                                
                    if event.key == pg.K_3:
                        if world.Line == False:
                            world.Line = True
                            world.Poly = False
                            world.Circle = False

                    if event.key == pg.K_d:
                        if world.Poly == True and self.onpol == True:
                            world.r = world.r + 1

                        elif world.Poly == True and self.oncircle == True:
                            world.mass = world.mass + 1


                        elif world.Circle == True and self.onpol == True:
                            world.ball_rad = world.ball_rad + 1   

                        elif world.Circle == True and self.oncircle == True:
                            world.ball_mass = world.ball_mass + 1


                        elif world.Line == True and self.onpol == True:
                            world.line_rad = world.line_rad + 1


                        elif world.Line == True and self.oncircle == True:
                            world.line_mass = world.line_mass + 1 


                        elif world.Line == True and self.onlien == True:
                            world.line_dli = world.line_dli + 1


                    if event.key == pg.K_a:
                        if world.Poly == True and self.onpol == True:
                            world.r = world.r - 1
                            if world.r < 1:
                                world.r = 1

                        elif world.Poly == True and self.oncircle == True:
                            world.mass = world.mass - 1
                            if world.mass < 1:
                                world.mass = 1

                        elif world.Circle == True and self.onpol == True:
                            world.ball_rad = world.ball_rad - 1   
                            if world.ball_rad < 1:
                                world.ball_rad = 1

                        elif world.Circle == True and self.oncircle == True:
                            world.ball_mass = world.ball_mass - 1
                            if world.ball_mass < 1:
                                world.ball_mass = 1   

                        elif world.Line == True and self.onpol == True:
                            world.line_rad = world.line_rad - 1
                            if world.line_rad < 1:
                                world.line_rad = 1

                        elif world.Line == True and self.oncircle == True:
                            world.line_mass = world.line_mass - 1 
                            if world.line_mass < 1:
                                world.line_mass = 1

                        elif world.Line == True and self.onlien == True:
                            world.line_dli = world.line_dli - 1
                            if world.line_dli < 1:
                                world.line_dli = 1

                    if event.key == pg.K_s:
                        if self.onpol == True:
                            self.r3 = 250
                            self.oncircle = True
                            self.r1 = 50
                            self.onpol = False

                        elif self.oncircle == True and world.Line == True:
                            self.r = 250
                            self.onlien = True
                            self.r3 = 50
                            self.oncircle = False

                        elif self.oncircle == True and world.Line != True:
                            self.r1 = 250
                            self.onpol = True
                            self.r3 = 50
                            self.oncircle = False

                        elif self.onlien == True and world.Line == True:
                            self.r1 = 250
                            self.onpol = True 
                            self.r = 50
                            self.onlien = False 

                    if event.key == pg.K_w:
                        if self.onpol == True and world.Line == True:
                            self.r = 250
                            self.onlien = True
                            self.r1 = 50
                            self.onpol = False

                        elif self.onpol == True and world.Line != True:
                            self.r3 = 250
                            self.oncircle = True
                            self.r1 = 50
                            self.onpol = False

                        elif self.onlien == True and world.Line == True:
                            self.r3 = 250
                            self.oncircle = True  
                            self.r = 50        
                            self.onlien = False

                        elif self.oncircle == True:
                            self.r1 = 250
                            self.onpol = True
                            self.r3 = 50
                            self.oncircle = False    

                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pg.mouse.get_pos()
                        world.pick_free_prop(space, mouse_pos)

                    if event.button == 3:
                        prop = shape_creator.create_free_prop(mouse_pos[0], mouse_pos[1])

                if event.type == pg.MOUSEBUTTONUP:
                    world.release_picked_prop()

            space.step(1/self.fps)
            #debug props

            #print(str(len(space.bodies)) + '    ' + str(len(world.free_props)))

            shape_creator.remove_noclipped_props()

            mouse_pos = pg.mouse.get_pos()
            world.move_picked_prop(mouse_pos)

            world.fill_me()

            camera.fill([250,250,250])    

            space.debug_draw(draw_options)

            world.blit_me()

            self.show_fps(camera, clock, font)
            self.show_prop(camera, fon, world)
            pg.display.flip()
            clock.tick(self.fps)   

    def show_fps(self,camera,clock,font):
        fps = font.render('{0:.2f}'.format(clock.get_fps()), True, [50,50,50])
        camera.blit(fps, [10,10])

    def show_prop(self,camera,fon,world):
        pop = fon.render("Prop", True, [50,50,50] )
        camera.blit(pop, [self.camera_width/2-90,10])
        pip = fon.render("radius: ", True, [self.r1,self.g1,self.b1])
        camera.blit(pip, [self.camera_width/2+450, 10])
        nipi = fon.render("mass: ", True, [self.r3,self.g3,self.b3])
        camera.blit(nipi, [self.camera_width/2+450, 40])


        if world.Poly == True:
            pol = fon.render("Square", True, [50,50,50] )
            camera.blit(pol, [self.camera_width//2-100,50])
            num = fon.render(str(world.mass), True, [50,50,50] )
            nun = fon.render(str(world.r), True, [50,50,50] )
            camera.blit(num, [self.camera_width/2+515, 40])
            camera.blit(nun, [self.camera_width/2+535, 10])

        elif world.Circle == True:
            cir = fon.render("Circle", True, [50,50,50])
            camera.blit(cir,[self.camera_width//2-100,50])
            nym = fon.render(str(world.ball_mass), True, [50,50,50] )
            ngm = fon.render(str(world.ball_rad), True, [50,50,50] )
            camera.blit(nym, [self.camera_width/2+515, 40])
            camera.blit(ngm, [self.camera_width/2+535, 10])


        elif world.Line == True:
            line = fon.render("Line", True, [50,50,50])
            camera.blit(line,[self.camera_width//2-90,50])

            nm =  fon.render(str(world.line_mass), True, [50,50,50] )
            nw =  fon.render(str(world.line_rad), True, [50,50,50] )
            fo =  fon.render(str(world.line_dli), True, [50,50,50] )
            bo = fon.render('length: ', True, [self.r,self.g,self.b])

            camera.blit(nm, [self.camera_width/2+515, 40])
            camera.blit(nw, [self.camera_width/2+535, 10] )
            camera.blit(bo, [self.camera_width/2+450, 70])
            camera.blit(fo, [self.camera_width/2+535, 70])


if __name__ == '__main__':
    new_game = Game()
    new_game.game_ini()
