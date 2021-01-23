from assets.classes.textview import *
from assets.styles.default import *
from assets.classes.snake import *

def game(pygame, screen, exit):
	#constants
	fps = int(1000/10)
	worldWidth = 16
	worldHeight = 12
	cellSize = 36
	headStartPos = [4, 4]

	#intances
	world = World(worldWidth, worldHeight, cellSize, Default.emptycell_color, Default.snakecell_color, Default.food_color)
	snake = Snake(worldWidth, worldHeight, headStartPos)

	def pause():
		#textviews
		textviews = {
			'resume' : Textview(70, 100, Default.tv_spacing_small, "Resume", Default.tv_style_primary),
			'restart' : Textview(70, 150, Default.tv_spacing_small, "Restart", Default.tv_style_primary),
			'mainmenu' : Textview(70, 200, Default.tv_spacing_small, "Main menu", Default.tv_style_primary)
		}
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: return 0
				mousePos = pygame.mouse.get_pos()
				for name, textview in textviews.items():
					if textview.getRect().collidepoint(mousePos):
						if event.type == pygame.MOUSEBUTTONDOWN:
							textview.click()
							if name=="resume": return 0
							if name=="restart": return 1
							elif name=="mainmenu": return 2
						else:
							textview.hover()
					else:
						textview.default()
			
			#draw textviews
			[textviews[name].draw(screen) for name in textviews]

			pygame.display.flip()
			pygame.time.delay(fps)

	#textviews
	textviews = {
		'gamescore' : Textview(0, 400, Default.tv_spacing_small, str(world.getScore()), Default.tv_style_gamescore)
	}
	while 1:
		#get all pressed keys
		pressedKeys = pygame.key.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					r = pause()
					if r==0: pass
					if r==1:
						world.reset()
						snake.reset()
					elif r==2: return 0

		if pressedKeys != None:
			if pressedKeys[pygame.K_w]: snake.setDirection(1)
			elif pressedKeys[pygame.K_a]: snake.setDirection(2)
			elif pressedKeys[pygame.K_s]: snake.setDirection(3)
			elif pressedKeys[pygame.K_d]: snake.setDirection(0)

		screen.fill(Default.game_bg_color)

		snake.move()
		updateResponse = world.update(snake.getInfo())
		if updateResponse==0: pass
		elif updateResponse==1:
			snake.grown()
			textviews["gamescore"].setText(str(world.getScore()))
		elif updateResponse==2: return 0
		world.draw(screen);

		#draw textviews
		[textviews[name].draw(screen) for name in textviews]
		
		pygame.display.flip()
		pygame.time.delay(fps)
