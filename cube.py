import turtle
import math

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("gray")  # Set background to gray
screen.title("Cube")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define cube vertices
vertices = [
    [-100, -100, -100], [100, -100, -100], [100, 100, -100], [-100, 100, -100],
    [-100, -100, 100], [100, -100, 100], [100, 100, 100], [-100, 100, 100]
]

# Edges connecting the vertices
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]


# Rotate around X-axis
def rotateX(point, angle):
    rad = math.radians(angle)
    cosA = math.cos(rad)
    sinA = math.sin(rad)
    y = point[1] * cosA - point[2] * sinA
    z = point[1] * sinA + point[2] * cosA
    return [point[0], y, z]


# Rotate around Y-axis
def rotateY(point, angle):
    rad = math.radians(angle)
    cosA = math.cos(rad)
    sinA = math.sin(rad)
    x = point[0] * cosA + point[2] * sinA
    z = -point[0] * sinA + point[2] * cosA
    return [x, point[1], z]


# Rotate around Z-axis
def rotateZ(point, angle):
    rad = math.radians(angle)
    cosA = math.cos(rad)
    sinA = math.sin(rad)
    x = point[0] * cosA - point[1] * sinA
    y = point[0] * sinA + point[1] * cosA
    return [x, y, point[2]]


# Project 3D point to 2D
def project(point):
    distance = 300
    factor = distance / (distance - point[2])
    x = point[0] * factor
    y = point[1] * factor
    return [x, y]


# Draw the cube
def draw_cube():
    t.clear()
    # Rotate the cube
    rotated_vertices = [rotateX(rotateY(rotateZ(v, angleZ), angleY), angleX) for v in vertices]
    projected_vertices = [project(v) for v in rotated_vertices]

    # Draw edges
    for edge in edges:
        t.penup()
        t.goto(projected_vertices[edge[0]][0], projected_vertices[edge[0]][1])
        t.pendown()
        t.goto(projected_vertices[edge[1]][0], projected_vertices[edge[1]][1])

    # Fill
    t.penup()
    for x in range(-50, 81, 40):  # Adjust range and step
        for y in range(-50, 81, 40):
            for z in range(-50, 81, 40):
                rotated_point = rotateX(rotateY(rotateZ([x, y, z], angleZ), angleY), angleX)
                projected_point = project(rotated_point)
                t.goto(projected_point[0], projected_point[1])
                t.write("Cube", align="center", font=("Arial", 12, "normal"))

    screen.update()


# Init rotation x,y,z
angleX = 0
angleY = 0
angleZ = 0


# Loop
def animate():
    global angleX, angleY, angleZ
    angleX += 2
    angleY += 3
    angleZ += 1
    draw_cube()
    screen.ontimer(animate, 50)

# Init 
screen.tracer(0)
animate()
screen.mainloop()