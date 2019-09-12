import math

# Input values: define the given forces below
force1=1.47
angle1=0
force2=1.22
angle2=85

# convert input degrees to radians
angle1rad=angle1*2*math.pi/360
angle2rad=angle2*2*math.pi/360

# break forces into compoents
force1x=math.sin(angle1rad)*force1
force2x=math.sin(angle2rad)*force2
force1y=math.cos(angle1rad)*force1
force2y=math.cos(angle2rad)*force2

# calculate magnitude of third force
force3=math.sqrt((force1x+force2x)**2+(force1y+force2y)**2)

# determine what mass is needed to make force3
mass=force3/9.8

# calculate angle of third force in radians
angle3rad=math.atan((force1x+force2x)/(force1y+force2y))+math.pi

# convert angle of third force to degrees
angle3=angle3rad*360/(2*math.pi)

# print the two results
print(mass,angle3)