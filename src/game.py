### GAME OPTION SELECTION DICTS ###

#Each room is a list of dicts, with the keys being the options the player can choose from, and their values being the response for each option
#response[0] = "text output"
#response[1] = "room to send player to"
#response[2+n] = "item and event triggers

#the '@' symbol is used to mark a conditional segment
#items and events are checked in conditional segments using "==" and "!="
#conditions can be chained together with "and" along with "or"
#Conditional text is placed in '{}'

#item and event values can be set with "="

ROOM1 = {
  "help":["You are alone in the forest. It is raining. There something off to the North in the distance.", "room1"],
  "look":["On the ground there is a stump@seeds == no{ next to some seeds}. The stump appears talktative.", "room1"],
  "talk":["The stump tells you it wants soup.", "room1"],
  "give soup":["@soup == no{You have no soup.}@soup == yes{The stump consumes the soup and grows into a large tree.}", "@soup == no{room1}@soup != no{room4}", "@soup == yes{soup = used}"],
  "grab seeds":["@seeds == no{You pick up the seeds.}", "room1", "@seeds == no{seeds = yes}"],
  "go north":["You go North.", "room2"],
}

ROOM2 = {
  "help":["You stand in the middle of a quiet clearing. Further in the North there is a structure.@seeds == yes and event_chicken == 1no{ You are being watched.}", "room2"],
  "look":["@seeds == no or event_chicken == 1yes and check == no{There is a blank check.}@seeds == no or event_chicken == 1yes and check == no and feather == no and event_chicken == 1yes{ }@feather == no and event_chicken == 1yes{There is a feather.}@seeds == yes and event_chicken == 1no{A chicken attacks you.}", "@event_chicken == 1yes or seeds == no{room2}@seeds == yes and event_chicken == 1no{room2_fight}"],
  "go south":["You go South", "room1"],
  "grab check":["@check == no{You pick up the blank check}", "room2", "@check == no{check = yes}"],
  "grab feather":["@feather == no and event_chicken == 1yes{You pick up the feather.}", "room2", "@feather == no{feather = yes}"],
  "go north":["You go North.", "room3"],
}

ROOM2_FIGHT = {
  "help":["It wants your seeds. Will you give the chicken the chicken your seeds, or fight?"],
  "fight":["You fight the chicken for your seeds and win. It runs aways and drops one of its feathers on the ground.","room2", "event_chicken = 1yes", "event_chicken = 2won"],
  "give seeds":["You give the chicken your seeds. It runs away but drops one of its feathers on the ground.","room2", "seeds = used", "event_chicken = 1yes", "event_chicken = 2lost"],
}

ROOM3 = {
  "help":["There is a booth out in the open getting drenched by rain.", "room3"],
  "look":["You see a scared and incompetent man standing in the booth. Maybe you could talk to him?", "room3"],
  "talk":["\"You look miserable in this downpour Mr.Bear. If you want some soup just ask.\"", "room3"],
  "ask":["\"I've got a bowl right here for you. We accept checks as payment, and nothing else.@check == no or check == used or feather == no{ But oh wait, you don't have any way to write me a check.}@check == yes and feather == yes{ Take some of this ink on my desk pay up.}\"", "room3"],
  "pay up":["@check == yes and feather == yes{\"Here you go. One hot soup!\"}", "room3", "@check == yes and feather == yes{soup = yes}", "@check == yes and feather == yes{check = used}"],
  "go south":["You go South", "room2"],
}

ROOM4 = {
  "help":["You stand atop a tree.", "room4"],
  "look":["Something flies towards you.", "room4_bird"],
}

ROOM4_BIRD = {
  "help":["A bird stands before you. It clearly has something to say.", "room4_bird"],
  "talk":["\"Howdy Partner. Now say I says I, you look like you ought a be going somewhere. I'll take you where you want to go, but you'll have to give me some seeds for the trouble. You got the goods?\"", "room4_bird"],
  "yes":["@event_chicken == 2won{\"Thanks a million. I'll take you to you're destination.\"}@event_chicken == 2lost{\"No you don't, but I admire your ability to lie. I'll gladly take you to your destination, because us liars have been ostracized for far too long.\"}", "room5", "event_bird = 2friend", "event_bird = 1yes", "seeds = used"],
  "no":["@event_chicken == 2lost{\"No seeds, no service. Sorry feller, I gotta get rid of you now.\"}@event_chicken == 2won{\"You silly potato, I see those seeds of yours right in your pocket. But since you don't want to cooperate I'll just take them from you and knock you into that river down there.\"} The bird quickly knocks you off into the river below. You try to look around, but the sound of running water puts you to sleep. The last thing you see is a small cod.", "room5", "event_bird = 2foe", "event_bird = 1yes", "seeds = used"],
}

ROOM5 = {
  "help":["@event_bird == 2foe and event_bear != 1yes{The small cod has swam }@event_bird == 2friend and event_bear != 1yes{The bird has flown }you to Fort Paddington.","room5"],
  "look":["@event_bear != 1yes{You see your nemesis Paddington Bear staring you down. You know that now, you must fight him.}", "room5"],
  "fight":["@event_bird == 2foe and event_bear != 1yes{You fish slap Paddington Bear and he spontaneously combusts.}@event_bird == 2friend and event_bear != 1yes{The bird pecks Paddinton Bear in the belly button and he turns into a jar of marmelaid which then spontaneously combusts.}@event_bear != 1yes{ A trophy appears where Paddington Bear used to stand. Grab it and victory will be yours.}", "room5", "event_bear = 1yes", "event_bear = 2won"],
  "grab trophy":["@event_bear == 1yes{\n- - - - - - - THANKS FOR PLAYING! - - - - - - -\n}","room5", "@event_bear == 1yes{trophy = yes}"],
}

### ROOM DICT ###

GAME_OPTIONS = {
  "room1":ROOM1,
  "room2":ROOM2,
  "room2_fight":ROOM2_FIGHT,
  "room3":ROOM3,
  "room4":ROOM4,
  "room4_bird":ROOM4_BIRD,
  "room5":ROOM5,
}

### PLAYER ITEMS AND EVENT DICTS ###

#item:("no", "yes", "used")
player_inventory = {
  "seeds":"no",
  "check":"no",
  "feather":"no",
  "soup":"no",
  "trophy":"no",
}

#event:[("no", "yes"), (outcome)]
player_events = {
  "event_chicken":["no", ""],
  "event_bird": ["no", ""],
  "event_bear": ["no", ""],
}
