from game import player_inventory

#COMMAND FUNCTIONS
#commands the player can access that aren't room specific

def print_inventory ():
  i = 0
  for item in player_inventory:
    if player_inventory.get(item) == "yes":
      i += 1
      if i == 1:
        print("INVENTORY:")
      print(str(i)+". %s" % item.upper())
  if i == 0:
    print("YOU AREN'T CARRYING ANY ITEMS.")

def exit_game ():
  while True:
    player_choice = input("DO YOU WANT TO END THE GAME? (yes or no)\n>").lower()
    if player_choice == "yes":
      print("\n- - - - - - - THANKS FOR PLAYING! - - - - - - -\n")
      exit()
    elif player_choice == "no":
      print("Continuing Game...")
      break

### COMMAND LIST ###

GAME_COMMANDS = {
  "inventory":print_inventory,
  "exit":exit_game,
}
