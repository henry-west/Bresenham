#Python v2.7
#Author: Henry West
#Example of Bresenham's Line Algorithm

import sys
#matplotlib.pyplot as plt
vertices = []
modifiedXY = []
#Convert printed coordinates
def convertSol(x,y, octant):
    if octant == 0:
        print "(",x + modifiedXY[0],",",y + modifiedXY[1],")"
    elif octant == 1:
        print "(",y + modifiedXY[0],",",x + modifiedXY[1],")"
    elif octant == 2:
        print "(",-1*y + modifiedXY[0],",",x + modifiedXY[1],")"
    elif octant == 3:
        print "(",-1*x + modifiedXY[0],",",y + modifiedXY[1],")"
    elif octant == 4:
        print "(",-1*x + modifiedXY[0],",",-1*y + modifiedXY[1],")"
    elif octant == 5:
        print "(",-1*y + modifiedXY[0],",",-1*x + modifiedXY[1],")"
    elif octant == 6:
        print "(",y + modifiedXY[0],",",-1*x + modifiedXY[1],")"
    elif octant == 7:
        print "(",x + modifiedXY[0],",",-1*y + modifiedXY[1],")"

#Bresenham's algorithm
def printPoints(x1,y1,x2,y2,octant):

    dx = x2-x1
    dy = y2-y1
    f = 2*dy - dx

    print "Octant: ",octant
    print "Endpoint for Calc:\t(",x2,",",y2,")"

    while x1 <= x2 and y1 <= y2:

        convertSol(x1,y1,octant)

        if f < 0:
            f += 2*dy
        else:
            f += 2*(dy - dx)
            y1 += 1
        x1 += 1

#Function to change endpoint of line to plot
def switchOctant():

    x1 = vertices[0]
    y1 = vertices[1]

    x2 = vertices[2]
    y2 = vertices[3]
    print "Original vertices:\t(",x1,",",y1,") to (",x2,",",y2,")"

    dx = x2-x1
    dy = y2-y1

    print "dx: ",dx
    print "dy: ",dy

	# Octants:
 	# \2|1/
 	# 3\|/0
 	#---+---
 	# 4/|\7
 	# /5|6\

	#octant 0
    if dx > dy and dy >= 0:
        printPoints(x1, y1, x2, y2,0)
	#octant 1
    elif dy >= dx and dx > 0:
        printPoints(x1, y1, y2, x2,1)
	#octant 2
    elif dx < 0 and dy > 0 and dy > abs(dx):
        printPoints(x1, y1, y2, -1*x2,2)
	#octant 3
    elif dx < 0 and dy > 0 and abs(dx) > dy:
        printPoints(x1, y1, -1*x2, y2,3)
	#octant 4
    elif dx < 0 and dy < 0 and abs(dx) > abs(dy):
        printPoints(x1,y1, -1*x2, -1*y2,4)
	#octant 5
    elif dx < 0 and dy < 0 and abs(dy) > abs(dx):
        printPoints(x1,y1, -1*y2, -1*x2,5)
	#octant 6
    elif dy < 0 and dx > 0 and abs(dy) > dx:
        printPoints(x1,y1, -1*y2, x2,6)
	#octant 7
    elif dy < 0 and dx > 0 and dx > abs(dy):
        printPoints(x1,y1, x2, -1*y2,7)

if len(sys.argv) == 5:
    vertices.append(0)
    vertices.append(0)
    vertices.append(int(sys.argv[3]) - int(sys.argv[1]))
    vertices.append(int(sys.argv[4]) - int(sys.argv[2]))

    modifiedXY.append(int(sys.argv[1]))
    modifiedXY.append(int(sys.argv[2]))

    switchOctant()
else :
    print"Add arguments for endpoints from the command line"
    print"e.g. ~$ python <path to program> <xEndpoint> <yEndpoint>"



