# import turtle
#
# # initial position
# turtle.penup()
# turtle.goto(10, -10)
# turtle.pendown()
#
# # Flower base
# turtle.fillcolor("red")
# turtle.begin_fill()
# turtle.circle(10, 180)
# turtle.circle(25, 110)
# turtle.left(50)
# turtle.circle(60, 45)
# turtle.circle(20, 170)
# turtle.right(24)
# turtle.fd(30)
# turtle.left(10)
# turtle.circle(30, 110)
# turtle.fd(20)
# turtle.left(40)
# turtle.circle(90, 70)
# turtle.circle(30, 150)
# turtle.right(30)
# turtle.fd(15)
# turtle.circle(80, 90)
# turtle.left(15)
# turtle.fd(45)
# turtle.right(165)
# turtle.fd(20)
# turtle.left(155)
# turtle.circle(150, 80)
# turtle.left(50)
# turtle.circle(150, 90)
# turtle.end_fill()
#
# # Petal 1
# turtle.left(150)
# turtle.circle(-90, 70)
# turtle.left(20)
# turtle.circle(75, 105)
# turtle.setheading(60)
# turtle.circle(80, 98)
# turtle.circle(-90, 40)
#
# # Petal 2
# turtle.left(180)
# turtle.circle(90, 40)
# turtle.circle(-80, 98)
# turtle.setheading(-83)
#
# # Leaves 1
# turtle.fd(30)
# turtle.left(90)
# turtle.fd(25)
# turtle.left(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.circle(-80, 90)
# turtle.right(90)
# turtle.circle(-80, 90)
# turtle.end_fill()
# turtle.right(135)
# turtle.fd(60)
# turtle.left(180)
# turtle.fd(85)
# turtle.left(90)
# turtle.fd(80)
#
# # Leaves 2
# turtle.right(90)
# turtle.right(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.circle(80, 90)
# turtle.left(90)
# turtle.circle(80, 90)
# turtle.end_fill()
# turtle.left(135)
# turtle.fd(60)
# turtle.left(180)
# turtle.fd(60)
# turtle.right(90)
# turtle.circle(200, 60)
#
# # End drawing
# turtle.done()
# import turtle
#
# screen = turtle.Screen()
# screen.bgcolor("white")
#
# flower = turtle.Turtle()
# flower.speed(10)
# flower.pencolor("purple")
#
# # Draw a single petal
# def draw_petal():
#     flower.circle(100, 60)
#     flower.left(120)
#     flower.circle(100, 60)
#     flower.left(120)
#
# # Draw all petals
# for _ in range(6):
#     draw_petal()
#     flower.left(60)
#
# # flower center
# flower.penup()
# flower.goto(0, -40)
# flower.pendown()
# flower.begin_fill()
# flower.color("yellow")
# flower.circle(40)
# flower.end_fill()
#
# # Hide turtle and wait for click
# flower.hideturtle()
# screen.exitonclick()
# class Car:
#     """A simple class to represent a car."""
#
#     def __init__(self, make, model, year, fuel_capacity_gallons=15):
#         """Initialize the car's attributes."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.fuel_capacity = fuel_capacity_gallons
#         self.fuel_level = fuel_capacity_gallons  # Start with a full tank
#
#     def get_description(self):
#         """Return a formatted description of the car."""
#         return f"{self.year} {self.make} {self.model}"
#
#     def fill_tank(self):
#         """Fill the car's fuel tank to capacity."""
#         self.fuel_level = self.fuel_capacity
#         print("Fuel tank is full.")
#
#     def drive(self, miles):
#         """Simulate driving the car for a given number of miles."""
#         fuel_needed = miles / 25  # Assuming 25 miles per gallon
#         if self.fuel_level >= fuel_needed:
#             self.fuel_level -= fuel_needed
#             print(f"Drove {miles} miles. Remaining fuel: {self.fuel_level:.2f} gallons.")
#         else:
#             print("Not enough fuel to complete the drive. Please refill.")
#
# # Example usage:
# my_car = Car("Tesla", "Model 3", 2023)
# print(f"My car is a {my_car.get_description()}.")
#
# my_car.drive(100)
# my_car.drive(500)
# my_car.fill_tank()
# my_car.drive(300)

# import turtle
#
# car = turtle.Turtle()
#
# # Below code for drawing rectangular upper body
# car.color('#008000')
# car.fillcolor('#008000')
# car.penup()
# car.goto(0, 0)
# car.pendown()
# car.begin_fill()
# car.forward(370)
# car.left(90)
# car.forward(50)
# car.left(90)
# car.forward(370)
# car.left(90)
# car.forward(50)
# car.end_fill()
#
# # Below code for drawing window and roof
# car.penup()
# car.goto(100, 50)
# car.pendown()
# car.setheading(45)
# car.forward(70)
# car.setheading(0)
# car.forward(100)
# car.setheading(-45)
# car.forward(70)
# car.setheading(90)
# car.penup()
# car.goto(200, 50)
# car.pendown()
# car.forward(49.50)
#
# # Below code for drawing two tyres
# car.penup()
# car.goto(100, -10)
# car.pendown()
# car.color('#000000')
# car.fillcolor('#000000')
# car.begin_fill()
# car.circle(20)
# car.end_fill()
# car.penup()
# car.goto(300, -10)
# car.pendown()
# car.color('#000000')
# car.fillcolor('#000000')
# car.begin_fill()
# car.circle(20)
# car.end_fill()
#
# car.hideturtle()


import turtle

# Create a turtle object
spidey = turtle.Turtle()
spidey.speed(0)  # Fastest speed
spidey.pensize(3)


# Function to draw a curved line for the mask
def draw_curve(t, radius, angle, direction):
    for _ in range(angle):
        t.forward(radius)
        if direction == "left":
            t.left(1)
        else:
            t.right(1)


# Draw the main red face
spidey.color("red")
spidey.begin_fill()
spidey.circle(100)
spidey.end_fill()

# Draw the white eyes
spidey.penup()
spidey.goto(-40, 60)
spidey.pendown()
spidey.color("white")
spidey.begin_fill()
spidey.left(55)
draw_curve(spidey, 1, 100, "right")
draw_curve(spidey, 1, 100, "left")
spidey.forward(70)
spidey.right(90)
draw_curve(spidey, 0.5, 100, "right")
draw_curve(spidey, 0.3, 50, "right")
spidey.forward(50)
spidey.right(47)
draw_curve(spidey, 0.1, 95, "right")
spidey.end_fill()

# Draw the second eye (similar to the first, adjusted for position)
spidey.penup()
spidey.goto(40, 60)
spidey.pendown()
spidey.color("white")
spidey.begin_fill()
spidey.right(55)  # Adjust starting angle
draw_curve(spidey, 1, 100, "left")  # Reverse direction
draw_curve(spidey, 1, 100, "right")  # Reverse direction
spidey.forward(70)
spidey.left(90)  # Adjust turn
draw_curve(spidey, 0.5, 100, "left")  # Reverse direction
draw_curve(spidey, 0.3, 50, "left")  # Reverse direction
spidey.forward(50)
spidey.left(47)  # Adjust turn
draw_curve(spidey, 0.1, 95, "left")  # Reverse direction
spidey.end_fill()

spidey.hideturtle()
turtle.done()