
import pygame,sys
from game import Game
from colors import Colors

pygame.init()

#UI design
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

#creates a 500 x 620 display (width by height)
screen = pygame.display.set_mode((500, 620))

#title of the window
pygame.display.set_caption("Python Tetris")

#Controls the games framerate
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT

#sets a timer to move the block down every 200 milliseconds
pygame.time.set_timer(GAME_UPDATE, 200)

#main game loop
while True:
	#creates a list for all events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			#tells the game to run until it is closed (base case for the game loop)
			if game.game_over == True:
				game.game_over = False
				game.reset()
				
			#detecting user inputs
			#Defines all of the keyboard inputs
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False:
			
			#gradually moves objects down the screen
			game.move_down()

	#Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	#UI colours
	screen.fill(Colors.dark_blue)
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))

#defines the display for when the game ends
	if game.game_over == True:
		screen.blit(game_over_surface, (320, 450, 50, 50))

	 #drawing the game
	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60)
	#sets the framerate to 60
