from game import GAME_OPTIONS, player_inventory, player_events
from game_cmd import GAME_COMMANDS
from game_func import prompt
from game_utils import parse_lex, print_parse
from os import system, name #for clearing terminal

#set necessary variables before game loop
current_room = "room1"
current_options = GAME_OPTIONS["room1"]
if name == "nt": #windows os check
  system("cls")
else:
  system("clear")
print("\n- - - - - STARTING BEARGAME:ADVENTURE - - - - -\n")
print(current_options["help"][0])

#game loop
while player_inventory["trophy"] != "yes": #grabbing the trophy item ends the game
  #recieving player input
  while True:
    prompt_response = prompt(current_options, GAME_COMMANDS)
    if prompt_response[0] != "INVALID":
      player_choice = prompt_response[1]
    else:
      continue
    if prompt_response[0] == "CMD": #player_choice was a command
      GAME_COMMANDS[player_choice]()
    elif prompt_response[0] == "OPT": #
      output = parse_lex(player_choice[0]) #output is the text that will be displayed to the player
      if output != "":
        print (output)
        break
  #setting events/item values
  for x in range(2, len(player_choice)): #the range of the item/event setting slots
    request = parse_lex(player_choice[x]).replace(' ', "") #easier to manage without spaces
    splice_idx = request.find('=') #'=' seperates item and status
    item = request[:splice_idx]
    status = request[splice_idx+1:]
    if item [0:5] == "event":
        player_events[item][int(status[0])-1] = status[1:]
    else:
      player_inventory[item] = status
  #setting current options for the player
  new_room = parse_lex(player_choice[1])
  current_options = GAME_OPTIONS[new_room]
  if current_room != new_room:
    print_parse(current_options["help"][0])
    current_room = new_room
#game ended
exit()
