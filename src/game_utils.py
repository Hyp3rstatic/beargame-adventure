from game_func import lex, parse
from game import player_inventory, player_events

### WRAPPER FUNCTIONS ###

#parse_lex: parses lex of input given player items and events
def parse_lex (player_choice):
  return parse(lex(player_choice), player_inventory, player_events)

#print_parse: prints parse of input from parse_lex
def print_parse (player_choice):
  print(parse_lex(player_choice))
