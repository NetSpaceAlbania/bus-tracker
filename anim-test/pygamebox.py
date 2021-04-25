# Filename: A16b_simple_airtrack_forces.py
# Written by: James D. Miller

"""
Air Track with point forces...
Self-contained pygame-based example of pybox2d.
This file is based on the simple_01.py example in the pybox2d example directory.
"""

import pygame
from pygame.locals import *

# import Box2D # The main library
from Box2D import *

# This maps Box2D.b2Vec2 to vec2, and so on. (confusing, so disabled it)
#from Box2D.b2 import *

#=====================================================================
# Classes
#=====================================================================

class fwQueryCallback(b2QueryCallback):
    # Checks for objects at particular locations (p) like under the cursor.
    
    def __init__(self, p): 
        super(fwQueryCallback, self).__init__()
        self.point = p
        self.fixture = None

    def ReportFixture(self, fixture):
        body = fixture.body
        if body.type == b2_dynamicBody:
            inside=fixture.TestPoint(self.point)
            if inside:
                self.fixture=fixture
                # We found the object, so stop the query
                return False
        # Continue the query
        return True

class Environment:

    def __init__(self, screensize_tuple, world):
        self.world = world
        
        self.viewZoom          = 10.0
        self.viewCenter        = b2Vec2(0, 0.0)
        self.viewOffset        = b2Vec2(0, 0)
        self.screenSize        = b2Vec2(*screensize_tuple)
        self.rMouseDown        = False
        # self.textLine           = 30
        # self.font               = None
        # self.fps                = 0      
        
        self.mouseJoint = None

        # Needed for the mousejoint
        self.groundbody = self.world.CreateBody()
        
        self.flipX = False
        self.flipY = True
        
        # pass viewZoom to init in DrawToScreen class. Call the DrawToScreen function by use of the "renderer" name.
        self.renderer = DrawToScreen(self.viewZoom)
        
        self.pointSize = 2.5
        
        self.colors={
            'mouse_point'     : b2Color(1,0,0),
            'bomb_center'     : b2Color(0,0,1.0),
            'joint_line'      : b2Color(0.8,0.8,0.8),
            'contact_add'     : b2Color(0.3, 0.95, 0.3),
            'contact_persist' : b2Color(0.3, 0.3, 0.95),
            'contact_normal'  : b2Color(0.4, 0.9, 0.4),
            'force_point'     : b2Color(0,1,0)
        }
        
    def MouseDown(self, p):
        """
        Indicates that there was a left click at point p (world coordinates)
        """

        # If there is already a mouse joint just get out of here.
        if self.mouseJoint != None:
            return

        # Create a mouse joint on the selected body (assuming it's dynamic)
        # Make a small box.
        aabb = b2AABB(lowerBound=p-(0.001, 0.001), upperBound=p+(0.001, 0.001))

        # Query the world for overlapping shapes.
        query = fwQueryCallback(p)
        self.world.QueryAABB(query, aabb)
        
        if query.fixture:
            body = query.fixture.body
            # A body was selected, create the mouse joint
            self.mouseJoint = self.world.CreateMouseJoint(
                    bodyA=self.groundbody,
                    bodyB=body, 
                    target=p,
                    maxForce=1000.0*body.mass)
            body.awake = True
    
    def MouseUp(self, p):
        """
        Left mouse button up.
        """     
        if self.mouseJoint:
            self.world.DestroyJoint(self.mouseJoint)
            self.mouseJoint = None
            
    def MouseMove(self, p):
        """
        Mouse moved to point p, in world coordinates.
        """
        self.mouseWorld = p
        if self.mouseJoint:
            self.mouseJoint.target = p
            
    def CheckKeys(self):
        """
        Check the keys that are evaluated on every main loop iteration.
        I.e., they aren't just evaluated when first pressed down
        """

        pygame.event.pump()
        self.keys = keys = pygame.key.get_pressed()
        if keys[self.Keys.K_LEFT]:
            self.viewCenter -= (0.5, 0)
        elif keys[self.Keys.K_RIGHT]:
            self.viewCenter += (0.5, 0)

        if keys[self.Keys.K_UP]:
            self.viewCenter += (0, 0.5)
        elif keys[self.Keys.K_DOWN]:
            self.viewCenter -= (0, 0.5)

        if keys[self.Keys.K_HOME]:
            self.viewZoom = 1.0
            self.viewCenter = (0.0, 20.0)
        
    def Keyboard_Event(self, key, down=True):
        global apply_jet_1_TF, apply_jet_2_TF
        if down:
            if key==K_z:       # Zoom in
                self.viewZoom = min(1.1 * self.viewZoom, 50.0)
            elif key==K_x:     # Zoom out
                self.viewZoom = max(0.9 * self.viewZoom, 0.02)
            elif key == K_f:
                # Toggle the force.
                apply_jet_1_TF = not apply_jet_1_TF
                #print "applying force 1"
            elif key == K_g:
                # Toggle the force.
                apply_jet_2_TF = not apply_jet_2_TF
                #print "applying force 2"
            else:
                pass
        # If up
        else:
            if key == K_f:
                # Toggle the force.
                apply_jet_1_TF = not apply_jet_1_TF
            elif key == K_g:
                # Toggle the force.
                apply_jet_2_TF = not apply_jet_2_TF
            else:
                pass
    
    def checkEvents(self):
        """
        Check for pygame events (mainly keyboard/mouse events).
        Passes the events onto the GUI also.
        """
        # print "checkEvents"
        for event in pygame.event.get():
            # print "event.type = ", event.type
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                print ("early bailout")
                return False
            elif event.type == KEYDOWN:
                self.Keyboard_Event(event.key, down=True)
            elif event.type == KEYUP:
                self.Keyboard_Event(event.key, down=False)
            elif event.type == MOUSEBUTTONDOWN:
                #print "in MouseButtonDown block"
                p = self.ConvertScreenToWorld(*event.pos)
                if event.button == 1: # left
                   self.MouseDown( p )
                elif event.button == 2: #middle
                    pass
                elif event.button == 3: #right
                    self.rMouseDown = True
                elif event.button == 4:
                    self.viewZoom *= 1.1
                    #print "self.viewZoom", self.viewZoom
                elif event.button == 5:
                    self.viewZoom /= 1.1
            elif event.type == MOUSEBUTTONUP:
                p = self.ConvertScreenToWorld(*event.pos)
                if event.button == 3: #right
                    self.rMouseDown = False
                else:
                    self.MouseUp(p)
            elif event.type == MOUSEMOTION:
                
                p = self.ConvertScreenToWorld(*event.pos)
                self.MouseMove(p)
                if self.rMouseDown:
                    print ("in mousemotion block", event.pos, event.rel[0], event.rel[1])
                    self.viewCenter -= (event.rel[0]/1.0, -event.rel[1]/1.0)    #... it was /5.0

        return True

    def ConvertScreenToWorld(self, x, y):
        # self.viewOffset = self.viewCenter - self.screenSize/2
        self.viewOffset = self.viewCenter
        return b2Vec2((x + self.viewOffset.x) / self.viewZoom, 
                           ((self.screenSize.y - y + self.viewOffset.y) / self.viewZoom))

    def ConvertWorldtoScreen(self, point):
        """
        Convert from world to screen coordinates.
        In the class instance, we store a zoom factor, an offset indicating where
        the view extents start at, and the screen size (in pixels).
        """
        
        # The zoom factor works to define and scale the relationship between pixels (screen) and meters (world). 
        
        self.viewOffset = self.viewCenter
        x = (point.x * self.viewZoom) - self.viewOffset.x
        if self.flipX:
            x = self.screenSize.x - x
        y = (point.y * self.viewZoom) - self.viewOffset.y
        if self.flipY:
            y = self.screenSize.y - y
        return (int(round(x)), int(round(y)))  # return tuple of integers

    def drawMouseJoint(self):
        if self.mouseJoint:
            p1_screen = self.ConvertWorldtoScreen(self.mouseJoint.anchorB)  #The point on the object converted to screen coordinates.
            p2_screen = self.ConvertWorldtoScreen(self.mouseJoint.target)   #The current mouse position converted to screen coordinates.

            self.renderer.DrawPoint(p1_screen, self.pointSize, self.colors['mouse_point'])
            self.renderer.DrawPoint(p2_screen, self.pointSize, self.colors['mouse_point'])
            self.renderer.DrawSegment(p1_screen, p2_screen, self.colors['joint_line'])
            
    def drawForcePoint(self, forcePoint_2d_m):
        forcePoint_screen = self.ConvertWorldtoScreen( forcePoint_2d_m)
        self.renderer.DrawPoint( forcePoint_screen, self.pointSize, self.colors['force_point'])
            
class DrawToScreen:

    def __init__(self, viewZoom):
        self.viewZoom = viewZoom
        self.surface = screen
    
    def DrawPoint(self, p, size, color):
        """
        Draw a single point at point p given a pixel size and color.
        """
        self.DrawCircle(p, size/self.viewZoom, color, drawwidth=0)
    
    def DrawSegment(self, p1, p2, color):
        """
        Draw the line segment from p1-p2 with the specified color.
        """
        pygame.draw.aaline(self.surface, color.bytes, p1, p2)

    def DrawCircle(self, center, radius, color, drawwidth=1):
        """
        Draw a wireframe circle given the center, radius, axis of orientation and color.
        """
        radius *= self.viewZoom
        if radius < 1: radius = 1
        else: radius = int(radius)

        pygame.draw.circle(self.surface, color.bytes, center, radius, drawwidth)

        
#=================================================================================
# Some functions
#=================================================================================
    
def AddCar(theWorld, bodies, x=0, vx=0, width=1, height=1, my_restitution=1.00):
    
    # Create a dynamic body
    dynamic_body = theWorld.CreateDynamicBody(position=b2Vec2(x, 0), angle=0, linearVelocity=b2Vec2(vx, 0))
    
    # Add to the bodies list
    bodies.append( dynamic_body)
    
    # And add a box fixture onto it (with a nonzero density, so it will move)
    dynamic_body.CreatePolygonFixture(box=(width, height), density=1.0, friction=0.00, restitution=my_restitution)

    # Note the area used in the mass calc will be area = (2 * w) * (2 * h)
    # Then mass = density * area
    print ("Mass data:", dynamic_body.mass)

#=================================================================================
# Main program
#=================================================================================

# --- constants ---
TARGET_FPS = 120
TIME_STEP = 1.0/TARGET_FPS
screenXY = SCREEN_WIDTH, SCREEN_HEIGHT = 1140, 480

# --- pygame setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Simple pygame example')
clock = pygame.time.Clock()

# --- pybox2d world setup ---
# Create the world
world = b2World(gravity=(-0.0, -10.0), doSleep=True)

# Initialize the environment object (kind of like my own framework).
e = Environment(screenXY, world)
#Keys = TheKeys()

# List of bodies.
bodies = []

# And a static body to be the base of the air track.
ground_body = world.CreateStaticBody(
    position=(0,0),
    shapes=b2PolygonShape(box=(150,0.5))
    )
bodies.append( ground_body)

# left bumper
air_track_bumper1 = world.CreateStaticBody(
    position=(0,0),
    shapes=b2PolygonShape(box=(0.5,5))
    )
bodies.append( air_track_bumper1)

# right bumper
air_track_bumper2 = world.CreateStaticBody(
    position=(100,0),
    shapes=b2PolygonShape(box=(0.5,5))
    )
bodies.append( air_track_bumper2) 
    
# Add cars to the track
x = 15
for j in range(5):
    x += 5
    vx = j + 2
    #vx = -6
    AddCar(world, bodies, x, vx, height=1.0, width=2.0, my_restitution=0.90)


colors = {
    b2_staticBody  : (255,255,255,255),
    b2_dynamicBody : (127,127,127,255),
}

# Initialize the jet toggles.
apply_jet_1_TF = False
apply_jet_2_TF = False

# --- main game loop ---
running = True
while running:

    # Use the Environment instance "e" to check events
    running = e.checkEvents()
    # e.CheckKeys()

    # Apply forces
    if apply_jet_1_TF:
        force_point_1_2d_m = bodies[5].GetWorldPoint(b2Vec2(2,0))
        bodies[5].ApplyForce(force=b2Vec2(0.0, 100.0), point=force_point_1_2d_m, wake=True)
    if apply_jet_2_TF:
        force_point_2_2d_m = bodies[5].GetWorldPoint(b2Vec2(-2,0))
        bodies[5].ApplyForce(force=b2Vec2(0.0, 100.0), point=force_point_2_2d_m, wake=True)
    
    # Make Box2D simulate the physics of our world for one step.
    # Instruct the world to perform a single step of simulation. It is
    # generally best to keep the time step and iterations fixed.
    # See the manual (Section "Simulating the World") for further discussion
    # on these parameters and their implications.
    world.Step(TIME_STEP, 10, 10)    
    
    screen.fill((0,0,0,0))
    # Draw the world
    for body in bodies: # or: world.bodies
        # The body gives us the position and angle of its shapes
        for fixture in body.fixtures:
            # The fixture holds information like density and friction,
            # and also the shape.
            shape = fixture.shape
            
            # This assumes that this is a polygon shape. (not good normally!)
            # We take the body's transform and multiply it with each 
            # vertex, and then convert from world to screen.
            
            # The "*" operators are overloaded from the class (operator overloading).
            
            vertices_screen = []
            for vertex_object in shape.vertices:
                vertex_world = body.transform * vertex_object  # Overload operation
                vertex_screen = e.ConvertWorldtoScreen( vertex_world) # This returns a tuple
                vertices_screen.append( vertex_screen) # Append to the list.
            
            pygame.draw.polygon(screen, colors[body.type], vertices_screen)

    # Draw mouse joint.
    e.drawMouseJoint()
    
    # Draw force points.
    if apply_jet_1_TF:
        e.drawForcePoint( force_point_1_2d_m)
    if apply_jet_2_TF:
        e.drawForcePoint( force_point_2_2d_m)

    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    clock.tick(TARGET_FPS)
    
pygame.quit()
print('Done!')
