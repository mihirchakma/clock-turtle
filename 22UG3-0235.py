import turtle
import tkinter
import datetime
import math


# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("SLTC-BAIT BATCH1 CLOCK")
img = tkinter.Image("photo", file="clock.png")
turtle._Screen._root.iconphoto(True, img)
screen.tracer(0)

# Very basic clock face
face = turtle.Turtle()
face.shape("circle")
face.color("gold")
face.fillcolor("gold")
face.shapesize(stretch_wid=3, stretch_len=3)
face.penup()

# Hour hand
hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.color("black")
hour_hand.shapesize(stretch_wid=0.3, stretch_len=8)
hour_hand.penup()

# Minute hand
minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.color("blue")
minute_hand.shapesize(stretch_wid=0.2, stretch_len=12)
minute_hand.penup()

# Second hand
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(stretch_wid=0.1, stretch_len=16)
second_hand.penup()

# Hour labels
hour_labels = turtle.Turtle()
hour_labels.color("black")
hour_labels.penup()
hour_labels.hideturtle()

# Added: Round circle border
border = turtle.Turtle()
border.hideturtle()
border.pensize(5)  # Adjust border thickness
border.penup()
border.goto(-1, -203)  # Center of the clock
border.color("#E3651D")  # Choose your preferred border color
border.pendown()
border.circle(215)  # Adjust circle size as needed

# Added: Digital clock display
digital_clock = turtle.Turtle()
digital_clock.color("black")
digital_clock.penup()
digital_clock.hideturtle()
digital_clock.goto(0, 250)

# Additional feature: Draw a date label
date_turtle = turtle.Turtle()
date_turtle.hideturtle()
date_turtle.color("black")
date_turtle.penup()
date_turtle.goto(0, -270)  # Position below the clock face
date_turtle.write(datetime.datetime.now().strftime("%B %d, %Y"), align="center", font=("Arial", 16, "normal"))

# Draw the hour labels
def draw_hour_labels():
    for i in range(1, 13):
        angle = math.radians(30 * i)
        x = 200 * math.sin(angle)
        y = 200 * math.cos(angle)
        hour_labels.goto(x, y)
        hour_labels.write(str(i), align="center", font=("Arial", 15, "bold"))

# Update the clock time
def update_clock():
    now = datetime.datetime.now()
    # Angles for each hand 
    hour_angle = (now.hour % 12) * 30 + now.minute / 2 # Consider the minutes here
    # minute_angle = now.minute * 6 
    minute_angle = now.minute * 6 + now.second * 0.1 # Consider the seconds here
    second_angle = now.second * 6 

    # Rotate the hands
    hour_hand.setheading(90 - hour_angle)
    minute_hand.setheading(90 - minute_angle)
    second_hand.setheading(90 - second_angle)

    # Update the date label display
    date_turtle.clear()  # Clear previous date
    date_turtle.write(datetime.datetime.now().strftime("%d %B %Y"), align="center", font=("Arial", 20, "normal"))

    # Update the digital clock display
    digital_clock.clear()
    digital_clock.write(now.strftime("%I:%M:%S %p"), align="center", font=("Arial", 16, "normal"))

    # Update the screen
    screen.update()

    # Call ontimer() again after 1 second
    screen.ontimer(update_clock, 1000)

# Draw the hour labels
draw_hour_labels()
# Update the clock
update_clock()
# Start main loop
screen.mainloop()


###############################################
# Name: Mihir Chakma (SLTC)                   #
# Student ID: 22UG3-0235                      #
###############################################
