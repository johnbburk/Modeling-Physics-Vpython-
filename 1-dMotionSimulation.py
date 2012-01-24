from __future__ import division
from visual import *
from physutil import *
from visual.graph import *

###SETUP

# Set window title
scene.title = "1-D motion simulation"

# Define scene objects
field = box(size=(300,10,100),color = color.green,opacity = 0.3)
ball = sphere(radius=5, color = color.blue)

# Set up graph and onscreen curve
graph = PhysGraph()
trail = curve(color = color.yellow, radius = 1)

# Define axis that marks the field (divide into 15 equal intervals)
#IMPORTANT Question: Why do you need 16 Markers to divide the field into 15 intervals? 
axis = PhysAxis(field, 16)

# Define time parameters
t=0 #starting time
deltat = 0.001  #time step

# Set timer in top right of screen
timerDisplay = PhysTimer(150,150)



###END OF SETUP

###SET INITIAL CONDITIONS

# Define physics parameters
mball=0.6 #mass of ball

#set initial conditions for object motion
field.pos = vector(0,0,0) #place center of field at (0,0,0)
ball.pos = vector(-150,0,0) #set starting position of ball as (-150,0,0)
vball = vector(30,0,0) #initial velocity of ball in (vx,vy,vz) form


#calculate time for object to cross the field (think carfully about assumptions here)
tf=field.size.x/vball.x

# Set up MotionMap to display breadcrumbs 
motionMap = MotionMap(ball, tf, 10, markerType="breadcrumbs",    #drop 10 breadcrumbs between t=0 and tf
                      labelMarkerOffset=vector(0,-20,0),         #put lables below the marker
                      dropTime=True, timeOffset=vector(0,35,0)) # put times above the marker
# Set up MotionMap to display velocity vectors
velocityMap = MotionMap(ball, tf,10, markerScale = 0.5,labelMarkerOrder = false)

###END INITIAL CONDITIONS


### MAIN UPDATE LOOP; perform physics updates and drawing
while ball.pos.x < 150:  #while the ball's x-position is less than 150
    # Required to make animation visible / refresh smoothly (keeps program from running faster than 1000 frames/s)
    rate(1000)    

    # Ball physics update
    ball.pos = ball.pos + vball*deltat

    # Update motion map, graph plot, onscreen trail
    motionMap.update(t)
    velocityMap.update(t, vball)
    
    graph.plot(t,ball.pos.x)  #this plots one point in the graph in (x,y) form
    trail.append(pos = ball.pos)

    # Timer update
    t = t + deltat
    timerDisplay.update(t)
    
###END MAIN UPDATE LOOP
###POST LOOP 
    
print t   #print the final time (Question: what should this be?)
print ball.pos  #print the final position (Question: What should this be?)
