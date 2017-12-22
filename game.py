from characters import *

def main():
    alice = Player("alice.png", "Alice", 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130)
    bob = NPC("bob.png", "Robert", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    print(alice.level)
    print(bob.level)
	
main()