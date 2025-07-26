# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
import random
print("Made by daveculp at https://github.com/daveculp/Mystify-Py")

def draw_scene():
	global screen 
	screen.fill((0, 0, 0))

	for shape in shapes:
		max_p = len(shape)
		for i, point in enumerate (shape):
			x1,y1= point[0]
			x2,y2= shape[(i+1)%max_p][0]
			for i in range(30):
				pygame.draw.line(screen, point[3], (x1+(5*i),y1-(5*i)), (x2-(5*i),y2+(5*i)) )

	
def move_objects():
	global points, points2, shapes
	for shape in shapes:
		for point in shape:
			point[0][0] += point[1]
			point[0][1] += point[2]
			
			if point[0][0] < 0:
				point[0][0] = 0
				point[1] *= -1
				point[3] = get_random_color()
			elif point[0][0] > WIDTH -1:
				point[0][0] = WIDTH-1
				point[1] *= -1
				point[3] = get_random_color()
				
			if point[0][1] < 0:
				point[0][1] = 0
				point[2] *= -1
				point[3] = get_random_color()
			elif point[0][1] > HEIGHT -1:
				point[0][1] = HEIGHT-1
				point[2] *= -1
				point[3] = get_random_color()
  
def get_random_color():
	return ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
pygame.init()

def get_random_point():
	return ( [random.randint(0,WIDTH-1), random.randint(0, HEIGHT-1)])
	
def get_random_shape(num_verts):
	
	for i in range(num_verts):
		pass
WIDTH = 2400
HEIGHT = 1600

# Set up the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# point variables
shape1= [ [ get_random_point(),4,4, get_random_color()],\
		[ get_random_point(),2,6, get_random_color()],\
		[ get_random_point(),4,4, get_random_color()],\
		[ get_random_point(),4,4, get_random_color()] ]

shape2= [ [ get_random_point(),4,4, get_random_color()],\
		[ get_random_point(),2,6, get_random_color()],\
		[ get_random_point(),4,4, get_random_color()],\
		[ get_random_point(),4,4, get_random_color()] ]

shape3= [ [ get_random_point(),3,4, get_random_color()],\
		[ get_random_point(),3,5, get_random_color()],\
		[ get_random_point(),2,4, get_random_color()],\
		[ get_random_point(),5,5, get_random_color()] ]      
		
shape4= [ [ get_random_point(),3,4, get_random_color()],\
		[ get_random_point(),3,5, get_random_color()],\
		[ get_random_point(),2,4, get_random_color()],\
		[ get_random_point(),5,5, get_random_color()] ] 
		
shape5= [ [ get_random_point(),3,4, get_random_color()],\
		[ get_random_point(),3,5, get_random_color()],\
		[ get_random_point(),2,4, get_random_color()],\
		[ get_random_point(),5,5, get_random_color()] ] 
		
shape6= [ [ get_random_point(),3,4, get_random_color()],\
		[ get_random_point(),3,5, get_random_color()],\
		[ get_random_point(),2,4, get_random_color()],\
		[ get_random_point(),5,5, get_random_color()] ] 
		
				  
shapes = [shape1,shape2,shape3, shape4,shape5, shape6]

		

clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
dt = 1
font = pygame.font.SysFont("Arial", 18)
print("Window set up!")
time.sleep(3)

while running:

	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
					running = False  # Set running to False to end the while loop.

	# Fill the background with white
	move_objects()
	draw_scene()
	
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	screen.blit(fps_text, (10, 0))

	# Flip the display
	dt = clock.tick(90)
	pygame.display.flip()

# Done! Time to quit.
pygame.quit()
