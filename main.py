## A Simple programe for drawing circles of different color using opencv and pyhton

# Importing required Libraries namely opencv and numpy
import cv2
import numpy as np

# Canvas on which drawing will done
canvas = np.ones([500,500,3],'uint8')*255

# Color, radius and intial coordinates of circles that will drawn
color = (0,255,0)
radius = 5
point = (0,0)

# Function to handle click events for drawing, changing color and erasing
def click(event,x,y,flags,param):
  # Making these variable global will let us change them whenever we want
  global point, pressed, color
  
  #On moving mouse(without click) circles will be drawn 
  if event == cv2.EVENT_MOUSEMOVE:
    point = (x,y)
    cv2.circle(canvas,point,radius,color,-1)

  # On pressing left button color will toggle between blue and green
  elif event == cv2.EVENT_LBUTTONDOWN:
    if color == (0,255,0):
      color = (255,0,0)
    else:
      color = (0,255,0)
  
  # on pressing right mouse button color will be changed to white which will work as eraser     
  elif event == cv2.EVENT_RBUTTONDOWN:
    color = (255,255,255)      

# Naming our output window for adding click function  
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Loop for drawing until 'q' is pressed for quitting
while True:
  #Showing canvas window on screen
  cv2.imshow("canvas", canvas)

  #Setting Wait key as 'q'
  ch = cv2.waitKey(1)
  if ch & 0xFF == ord('q'):
    break

# Close window on quitting
cv2.destroyAllWindows()

