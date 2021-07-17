import pygame
import os
import math
from pygame.constants import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT, KEYDOWN, MOUSEBUTTONDOWN
from pygame.time import Clock

WIDTH, HEIGHT = 1920, 1080

ICON_IMG = pygame.image.load(os.path.join("Sprites","treeIcon.png"))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recursive Fractal Trees")
pygame.display.set_icon(ICON_IMG)

FPS = 60

starterBranchLength = 500

branchColor = (255,255,255)

minBranchLength = 5

def DrawBranch(length,branch1End,Branch2End):
	cornerPos1 = (branch1End[0] / (math.pi / 4),branch1End[1] + (math.pi / 4))
	cornerPos2 = (-(Branch2End[0] / 1.5),Branch2End[1] - length / 1.5)
	pygame.draw.line(WINDOW,branchColor,(branch1End),cornerPos1,2)
	pygame.draw.line(WINDOW,branchColor,(Branch2End),cornerPos2,2)

	if length > minBranchLength:
		DrawBranch(length * 0.9,cornerPos1,cornerPos2)
	else:
		return 0

def newDrawBranch(length,branchEnd,piMultiplier):
	cornerPos = (branchEnd[0] / 2,branchEnd[1] + (-length / 2))
	pygame.draw.line(WINDOW,branchColor,(branchEnd),cornerPos,2)
	
	if length > minBranchLength:
		print(1)
		newDrawBranch(length * 0.67,cornerPos,piMultiplier + 1)
	else:
		return 0

def main():
	
	WINDOW.fill((0,0,0))
	Clock = pygame.time.Clock()
	run = True
	
	pygame.draw.line(WINDOW,branchColor,(WIDTH / 2,HEIGHT),(WIDTH / 2,HEIGHT - starterBranchLength),2)

	while run:

		Clock.tick(FPS)
		#Drawing Initial Branch
		#DrawBranch(starterBranchLength * 0.7,(WIDTH / 2,HEIGHT - starterBranchLength),(WIDTH / 2,HEIGHT - starterBranchLength))
		newDrawBranch(starterBranchLength * 0.7,(WIDTH / 2,HEIGHT - starterBranchLength),4)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.display.flip()
	
	pygame.quit()



if __name__ == "__main__":
	main()