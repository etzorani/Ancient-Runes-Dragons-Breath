from characters import *
import pygame

def init(screen_width, screen_height):
    pygame.init()
    
    game_display = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Ancient Runes: Newt's Eye")
    
    pygame.display.update()
    
    game_exit = False
    
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            
    pygame.quit()

def main():
    alice = Player("alice.png", "Alice", 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130)
    bob = NPC("bob.png", "Robert", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    print(alice.level)
    print(bob.level)
    pygame.quit()

init(1200, 800)