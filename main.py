### THIS IS PROJECT DONE IN PYTHON 2.7 WITH TURTLE AND IN TRINKET.IO (ONLINE CODE EDITOR)

## Import statements -- remind them to always put imports at the very top
import turtle
import math
import random


## Board set up -- REVIEW OF 2D ARRAYS 
## Ask students:
  ### How do 1D arrays work?
  ### What index to arrays start at?
  ### What is one sure way we can get the last index of an array?
  ### What function finds the length of the array?
  ### Test them on the indexes for certain positions in the 2D array
    ### I.E. what are the indices of the spot in the middle?
## Explain to them why we are using a 2D array 
  ### 2D array looks like a tic tac toe board in real life so its a good representation for the computer
  ### When the user picks a spot, we change the value in the ARRAY and DRAW SOMETHING ON SCREEN
  ### MAKE IT VERY CLEAR THAT WHAT HAPPENS ON SCREEN DOES NOT DIRECTLY CHANGE THE ARRAY AND VICE VERSA
      ### WE MAKE THAT CHANGE HAPPEN AND CONNECT THE CHANGES. THE COMPUTER DOES NOT KNOW
  ### Clarify again: computer does NOT know what our variables are for and doesn't know we're trying to play tic tac toe
  
board = [ ["0", "0", "0"], 
        ["0", "0", "0"], 
        ["0", "0", "0"]]
        
## Positions keeps track of coordinate of upper left corner of each position
### DETAILED EXPLANATION OF 3D ARRAYS NEEDED, explain to them it refers to [row][col][COORDINATES]
### Can help them do this with a loop if they're really interested, otherwise, just have them fill it out 
positions = [ [ [-100, 200], [0, 200], [100, 200] ], 
             [ [-100, 100], [0, 100], [100, 100]], 
             [[-100, 0], [0, 0], [100, 0]] ]


## REVIEW OF DOUBLE FOR LOOPS
## Ask students: 
  ### Where to start and end? 
  ### What should we name the variables for each of the loops?
  ### What are each of the loops in charge of 
  ### How do we access a specific value of a 2D array?
  ### Review of using randint
    ### Is using randint a good idea? Why/Why not?
for row in range(0, len(board[0])):
  for col in range(0, len(board[0])):
    board[row][col] = random.randint(1, 100);

## Booleans keep track of who's turn it is 
## We start off with user X going first
  ## If we wanted to start with user O, how would we change these variables?
userX_turn = True
userO_turn = False


## Function checks if any player has won
def checkWin():
  
  ## REVIEW 2D ARRAYS AGAIN, IF NECESSARY
  ## REVIEW OF IF STATEMENTS 
    ### Usage of ANDS and ORS
    ### Equality checking
    
  ## Review idea of TRANSITIVE PROPERTY; if student has trouble understanding 
  ## expand the if statements to make it more clear to the student
  
  
  ## Check the rows to see if there is a winner 
  ## What indices do we need to change? What indices do we keep constant?
  for col in range(0, len(board[0])):
    if board[col][0] == board[col][1] and board[col][1] == board[col][2]:
      print "User " + board[col][0] + " won!"
      return True
  
  ## Check the cols to see if there is a winer
  ## What indices do we need to change? What indices do we keep constant?
  for row in range(0, len(board[0])):
    if board[0][row] == board[1][row] and board[1][row] == board[2][row]:
      print "User " + board[0][row] + " won!"
      return True
  
  ## Check diagonals
  ## We choose to use hard values here because there aren't many positions to check
  ## Ask them: what indices are the diagonals?
  if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
    print "User " + board[0][0] + " won!"
    return True
  ## Check other diagonal as well
  if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    print "User " + board[0][2] + " won!"
    return True
    
  ## No winner
  ## Ask student: why do not need any else's in this function?
  ## Could we add else's? Would the function work? Would it better to add else's or leave them out?
  return False
    
  
def switchTurn():
  
  ## Controls who's turn it is
  ## Review of BOOLEANS and the not keyword 
  ## Why do we say 'not?' why don't we use if/else
  # Alternatively, let them come up with the code below and ask them
  # if there is any way for them to simplify the code?
  ## Push them towards getting rid of the '== True' and explain
  ## If student is having trouble, can keep the if/else statements instead of using not 
  # if userX_turn == True:
  #   userX_turn = False
  #   userO_turn = True
  # elif userO_turn == True:
  #   userX_turn = True
  #   userO_turn = False
    
  global userX_turn, userO_turn
  userX_turn = not userX_turn
  userO_turn = not userO_turn
  
## Deals with user input asking for row/col

def getInput(userTurn, val):
  ## REVIEW OF FUNCTIONS 
    ## why are we using a function to ask for input? Does this make things easier or harder for us?
    ## Reiterate idea of reusable code
    ## Have them write out the expanded version separately asking for a row or column first
    ## How does our code need to be modified so that it can be used for both the row and column?
  ## REVIEW PARAMETERS
    ## Parameter types
    ## What values do the parameters have each time the function is called?
    ## Where can we access parameters?
    ## Go over naming parameters if they're confused 
  ## Review return values as necessary
  print "User " + userTurn + " enter a " + val + "(1 - 3)"
  pos = int(raw_input())
  while(pos < 1 or pos > 3):
    print "User " + userTurn + " enter a " + val + "(1 - 3)"
    pos = int(raw_input())
  pos = pos - 1
  return pos
  
def userTurn():
  ## Allows each user to enter a row/col and checks if the position is valid
  ## Ask the student:
  ## How do we know if a position is valid? 
  ## What if the user picks a position that is out of bounds?
    ### Review WHILE LOOPS and NOT statements, inverting boolean expressions
  ## What should we do to the board once the user picks a spot
  ## What if the user picks a spot that is already taken?
  
  ## Review if statements, AND, and == if needed
  ## When should we switch the turn?
  
  global userX_turn, userO_turn, positions
  row = -1
  col = -1
  turn = "X"
  if userO_turn:
    turn = "O"
  row = getInput(turn, "row")
  col = getInput(turn, "col")
  while(board[row][col] == "X" or board[row][col] == "O"):
    print "Position already taken. Please choose a new position "
    row = getInput(turn)
    col = getInput(turn)
  
  if userX_turn:
    drawX(positions[row][col][0], positions[row][col][1])
    board[row][col] = "X"
  else:
    drawO(positions[row][col][0], positions[row][col][1])
    board[row][col] = "O"
  
  switchTurn()
  
def drawBoard():
  ## Draws the initial board using turtle
  ## REVIEW BASIC TURTLE FUNCTIONS:
    ## set pos (coordinates)
    ## heading (direction/orientation)
    ## penup/pendown
    ## HAVE THEM LOOK AT THE TURTLE DOCUMENTATION FOR PYTHON 2.7 (make sure its not Python 3)
  ## Can have them do trial and error to decide how to draw the grid as well 
  
  turtle.speed(0)
  ## Draw the horizontal lines 
  ## How can we optimize drawing the lines instead of drawing them individually (push them toward loop)
  for horizontal_lines in range(0, 2):
    turtle.penup()
    turtle.setpos(-100, 100 - (horizontal_lines*100))
    turtle.pendown()
    turtle.forward(300)
  turtle.setheading(270)
  
  ## Draw vertical lines
  ## Push them toward using loops
  for vertical_lines in range(0, 2):
    turtle.penup()
    turtle.setpos(0 + (vertical_lines * 100), 200)
    turtle.pendown()
    turtle.forward(300)
    
def drawX(x_cor, y_cor):
  ## Draws the X
  ## REVIEW PARAMETERS
  ## Ask: 
      ### How do we know where to draw the x?
      
  ## THIS WILL REQUIRE UNDERSTANDING DEGREES FOR SET HEADING
  ## if student is too confused/never introduced to degrees, can just give them the values as well
  ## for those more curious, you can quiz them a bit more about degrees :)
  
  ## Will also require understanding of geometry and working with the sqrt (diagonal)
  ## Otherwise, you can either let the student experiment with the size of the X OR give them the value
  ## but if curious, explain to them how to find the correct value to fill up the square properly
  turtle.penup()
  turtle.setpos(x_cor, y_cor)
  turtle.setheading(315)
  turtle.pendown()
  turtle.forward(100 * math.sqrt(2))
  turtle.penup()
  turtle.setheading(225)
  turtle.setpos(x_cor + 100, y_cor)
  turtle.pendown()
  turtle.forward(100 * math.sqrt(2))
  
def drawO(x_cor, y_cor):
  ## Draws the O
  ## Review turtle.circle function if necessary
  turtle.penup()
  
  ## Explain the set heading is just needed to make sure the circles are drawn correctly
  ## Changing the heading will change the location of the circle
  turtle.setheading(270)
  
  ## This value was found through experimentation. Let student experiment
  turtle.setpos(x_cor, y_cor - 50)
  turtle.pendown()
  turtle.circle(50)


#### GAME SET UP #### 
## Ask students:
  ## What is the first thing the game needs?
  ## When should we let the users play?
  ## When do we know when the game is over?
      ## How does checkWin() tell us when the game is over?
  ## How many times do we need to call each function, each round?
  ## Review WHILE LOOPS VS FOR LOOPS
  ## When do we use while loops? For loops? Why are we using a while loop here?
  ## What happens the condition of the while loop becomes false?
  
  ### THIS VERSION HAS NOT IMPLEMENTED TIES
  ### Ask students: HOW DO YOU CHECK IF THERE'S A TIE?
  ### How do we know if there's a tie? 
  
  ### HAVE THE STUDENT TEST! A LOT!
  ## Testing to make sure the O's and X's are placed in the correct positions
  ## Test to make sure both players can win and the game ends properly
  ## What happens if the user enters an invalid position?
  ## What happens if the user enters a position already taken?

drawBoard()
gameOver = checkWin()
while not gameOver:
  userTurn()
  gameOver = checkWin()
