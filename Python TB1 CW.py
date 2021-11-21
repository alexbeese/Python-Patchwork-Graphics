from graphics import *

patchColours=[]

def main():
    patchworkSize = getInputs()
    drawingPatches(patchworkSize)

def getInputs():
    while True:
        patchworkSize = int(input("""which of the following would you like for your patchwork size:
        1 - 5x5
        2 - 7x7
        >>"""))
        if patchworkSize == 1 or patchworkSize == 2:
            break
        else:
            print ("please enter a valid number\n")

    colourChoice = ["red", "green","blue", "magenta","orange","cyan"]
    while True:
        colour = int(input("""enter a colour of your choice from the following:
        1 - red
        2 - green
        3 - blue
        4 - magenta
        5 - orange
        6 - cyan
        >>"""))

        if colour >= 1 and colour <= 6:
            colour-=1
            #puts users colours into list
            patchColours.append(colourChoice[colour])

        #measures against wrong inputs
        if len(patchColours) == 3:
            if patchColours[0] == patchColours[1] and patchColours[1] == patchColours[2]:
                print ("you cannot have the same colour three times\n")
                patchColours.clear()
            else:
                print (f"your colour choices are: {patchColours[0]}, {patchColours[1]} and {patchColours[2]}")
                return patchColours
                break

def drawingPatches(patchworkSize):
    if patchworkSize == 1:
        winsize = 500
        winsize = GraphWin("patchwork",winsize,winsize)

    else:
        winsize = 700
        win = GraphWin("patchwork",winsize,winsize)
    win.setBackground("white")

    row = 0
    column = 0
    coord = 0

    #making grid
    for y in range(0,winsize,100):
        for x in range(0,winsize,100):

            chosenColour, chosenPattern, mainPattern = choose(winsize, row, column)

            if chosenPattern == 0:
                pattern9(chosenColour,win,x,y)
            else:
                pattern2(chosenColour,win,x,y)

            #using row and column to cycle through the 2d arrays
            #technique used for all arrays

            column+=1
            if column ==(len(mainPattern)):
                column=0
                row+=1
                if row==(len(mainPattern)):
                    row-=1

def choose(winsize, row, column):
    if winsize == 500:
        #numbers correspond to colour and patch patterns
        mainColours = [[0,1,1,1,1],[0,2,1,1,1],[0,2,0,1,1],[0,2,0,2,1],[0,2,0,2,0]]
        mainPattern = [[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]]
    else:
        mainColours = [[0,1,1,1,1,1,1],[0,2,1,1,1,1,1],[0,2,0,1,1,1,1],[0,2,0,2,1,1,1],[0,2,0,2,0,1,1],[0,2,0,2,0,2,1],[0,2,0,2,0,2,0]]
        mainPattern = [[0,1,1,1,1,1,1],[0,0,1,1,1,1,1],[0,0,0,1,1,1,1],[0,0,0,0,1,1,1],[0,0,0,0,0,1,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]]

    chosenColour = patchColours[mainColours[row][column]]
    chosenPattern = mainPattern[row][column]
    return (chosenColour, chosenPattern, mainPattern)



def pattern9(chosenColour, win, xoff, yoff): #penultimate digit
    mainPattern9 = [[1,0,1,0,1],[0,2,0,2,0],[1,0,1,0,1],[0,2,0,2,0],[1,0,1,0,1]]
    row = 0
    column = 0

    for y in range(0,100,20):
        for x in range(0,100,20):
            #offsets
            realx = x + xoff
            realy = y + yoff
            if mainPattern9[row][column] == 0:
                square = Rectangle(Point(realx,realy),Point(realx+20,realy+20))
                square.setFill(chosenColour)
                square.setOutline(chosenColour)
                square.draw(win)


            elif mainPattern9[row][column] == 1:
                circle = Circle(Point(realx+10,realy+10),10)
                circle.setFill(chosenColour)
                circle.setOutline(chosenColour)
                circle.draw(win)

                triangle = Polygon(Point(realx+10,realy+10),Point(realx+20,realy), Point(realx+20,realy+20))
                triangle.setFill("white")
                triangle.setOutline("white")
                triangle.draw(win)

            elif mainPattern9[row][column] == 2:
                circle = Circle(Point(realx+10,realy+10),10)
                circle.setFill(chosenColour)
                circle.setOutline(chosenColour)
                circle.draw(win)

                triangle = Polygon(Point(realx+10,realy+10),Point(realx,realy), Point(realx,realy+20))
                triangle.setFill("white")
                triangle.setOutline("white")
                triangle.draw(win)


            column+=1
            if column == 5:
                column=0
                row+=1
                if row ==5:
                    row-=1

def pattern2(chosenColour, win, xoff, yoff): #final digit
    mainPattern2 = [[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1]]
    row = 0
    column = 0

    for y in range(0,100,20):
        for x in range(0,100,20):
            #offsets
            realx = x + xoff
            realy = y + yoff
            #function to draw individual circles
            drawCircle(win,Point(realx+10,realy+10),10,chosenColour, mainPattern2, row, column)

            column+=1
            if column == 5:
                column=0
                row+=1
                if row ==5:
                    row-=1

def drawCircle(win, point, radius, chosenColour, mainPattern2, row, column,):
    circle = Circle(point, radius)

    #using list to know if circle should be coloured or white
    if mainPattern2[row][column] == 1:
        circle.setFill(chosenColour)
    else:
        circle.setFill("white")

    circle.setOutline(chosenColour)
    circle.draw(win)


main()