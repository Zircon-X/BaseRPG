#This program is going to be testing an astar algorithm of our own device.

from graphics import *
import random
'''	
	Width and height are variables used to calculate co-ordinates as well as set the size of the window
	gridsize is used to space gridlines as used in drawGrid, win simply sets the co-ordinates of the 
	window as well as its title. coord is a placeholder variable that will be reset at certain parts
	of the program.
'''
Width = 1000
Height = 1000
gridsize = 100
win = GraphWin('Grid', Width, Height) # give title and dimensions	
coord = Point(0, 0)
startCoords = Point(0, 0)
goalCoords = Point(0, 0)
obstacleCoords=[]
'''
	randomcoords is a function that produces a random co-ordinate when called. It returns the Point
	to the calling function at the end of the function.
'''
def randomcoords():
	xmax = Width/gridsize #Calculates maximum x co-ordinate by dividing window width by gridsize in pixels
	ymax = Height/gridsize #Calculates maximum y co-ordinate by dividing window width by gridsize in pixels
	xcomponent = random.randrange(0, xmax, 1) #chooses random x co-ordinate on grid.
	ycomponent = random.randrange(0, ymax, 1) #chooses random y co-ordinate on grid.
	finalxcoord = xcomponent * gridsize #converts co-ordinate back to pixels
	finalycoord = ycomponent * gridsize #converts coordinate back to pixels
	randpoint = Point(finalxcoord, finalycoord) #assigns x and y co-ordinate to a Point to be returned to calling function
	return randpoint

def drawGrid():
	currentGridX = 0 #variable used to hold current grid position on x axis.
	currentGridY = 0 #variable used to hold current grid position on y axis.
	while currentGridX <= Height: #This while loop draws the vertical lines to represent x co-ordinate
		gridlineX = Line(Point(currentGridX, 0), Point(currentGridX, Height))
		gridlineX.setOutline("Black")
		gridlineX.setFill("Black")
		gridlineX.draw(win)
		currentGridX += gridsize
	while currentGridY <= Width: #This while loop draws the horizontal lines to represent x co-ordinate
		gridlineY = Line(Point(0, currentGridY), Point(Width, currentGridY))
		gridlineY.setOutline("Black")
		gridlineY.setFill("Black")
		gridlineY.draw(win)
		currentGridY += gridsize
		
def placeStart(): #This function places the start node at a random location on the grid.
	startCoords = randomcoords() #retrieve a random set of co-ordinates
	Start = Circle(startCoords, 20) #place a circle of a 20 pixel radius at previously created co-ordinates
	Start.setOutline("Green") 
	Start.setFill("Green")
	Start.draw(win) #draw circle of Green outline and fill.
	
def placeGoal(): #This function places the Goal Node at a random location on the grid. 
	goalCoords = randomcoords() #retrieves a random set of co-ordinates
	Goal = Circle(goalCoords, 20) #places a circle of a 20 pixel radius at previously created co-ordinates.
	Goal.setOutline("Blue") 
	Goal.setFill("Blue")
	Goal.draw(win) #draw circle of Blue outline and fill.

def placeObstacles(): #This function places between 1 and 5 obstacles on the grid. A star will mark these as non-traversable.
	obstaclesPlaced = 0 #counter used in while loop to keep track of placed obstacles.
	numOfObstacles = random.randrange(1, 5, 1) #chooses number of obstacles.
	while obstaclesPlaced <= numOfObstacles: #This loop will run until the predetermined number of obstacles is placed.
		obstacleCoords = randomcoords() #Obtain random co-ordinates for obstacle.
		Obstacle = Circle(obstacleCoords, 20) #Places a circle with a radius of 20 pixels at co-ordinates
		Obstacle.setOutline("Red")
		Obstacle.setFill("Red")
		Obstacle.draw(win) #draw the circle with Red outline and fill.
		obstaclesPlaced += 1 #increment the number of obstacles placed.
		
def main(): 
	drawGrid() #draws Grid
	placeStart() #places Start Node
	placeGoal() #places Goal Node
	placeObstacles() #places Obstacle Nodes
	win.getMouse() #wait until click inside window to end. Without this, window closes immediately after last function call.


main()
