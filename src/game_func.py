#prompt: determine if player input is a command, a room option, or invalid
def prompt (player_options, command_list):
  player_choice = input('>').lower()
  if player_choice in command_list:
    return ["CMD", player_choice]
  elif player_choice in player_options:
    return ["OPT", player_options.get(player_choice)]
  else:
    return ["INVALID"]

#lex: turn string into tokenized list segments
#'V' is a condition segment token
#'CT' is conditional text token
#'A' is an "and" token
#'O' is an "or" token
#TODO: add parenthesis support
def lex (str):
  str_lex = [] #return value
  for x in range(0, str.count('@')): #repeat this loop for every conditional segment
      cond_seg = str.split('@', 1)
      str = cond_seg[1].split('{', 1)[1] #make str everything after the conditional segment as a way of holding the portion of the text that remains unlexed after this loop iteration
      if cond_seg[0] != "": #only append non-conditional text if it exists
        str_lex.append(cond_seg[0])
      str_lex.append('V')
      cond_seg = cond_seg[1].split('{', 1)[0] + '{' #cond_seg now only holds the conditional segment
      #replace "and", "or" with single character for char by char checking
      cond_seg = cond_seg.replace(" and ", '&')
      cond_seg = cond_seg.replace(" or ", '|')
      cond_split = cond_seg.replace(' ', "")
      for char in cond_seg:
        if char in ['&', '|', '{']:
          cond_split = cond_split.split(char, 1) #cond_split shortened to only the characters after the char that triggered the if statement
          #this allows split to be used with cond_split given a char found in cond_seg
          str_lex.append(cond_split[0]) 
          cond_split = cond_split[1]
          if char == '&':
            str_lex.append('A')
          elif char == '|':
            str_lex.append('O')
      str_lex.append('CT')
      str_lex.append(str.split('}', 1)[0])
      str = str.split('}', 1)[1]
  if str != "":
    str_lex.append(str)
  return str_lex

#TODO: add parenthesis support
#parse: resolve conditional statements given lexed input
def parse (str_lex, player_inventory, player_events):
  str_parse = str_lex #return value
  for x in range(0, str_parse.count('V')): #repeat this loop for every conditional segment
    start_idx = str_parse.index('V')
    end_idx = str_parse.index('CT')
    ver_seg = str_parse[start_idx+1:end_idx] #hold segment of conditions
    del str_parse[start_idx:end_idx+1] #start_idx becomes position of conditional text which can be deleted later if the condition equates to false
    for j in range(0, len(ver_seg), 2): #evaluate equality expressions
      full_condition = ver_seg[j]
      splice_idx = full_condition.find('!')
      if splice_idx == -1:
        splice_idx = full_condition.find('=')
      item = full_condition[:splice_idx]
      status = full_condition[splice_idx+2:]
      operator = full_condition[splice_idx]+'='
      if item [0:5] == "event": #handle events
        if operator == '==':
          ver_seg[j] = player_events.get(item)[int(status[0])-1] == status[1:]
        elif operator == '!=':
          ver_seg[j] = player_events.get(item)[int(status[0])-1] != status[1:]
      else: #handle items
        if operator == '==':
          ver_seg[j] = player_inventory.get(item) == status
        elif operator == '!=':
          ver_seg[j] = player_inventory.get(item) != status
    for j in range(1, len(ver_seg), 2): #evaluate logical operators given evaluated expressions
      if ver_seg[j] == 'A':
        ver_seg[j+1] = ver_seg[j-1] and ver_seg[j+1]
      if ver_seg[j] == 'O':
        ver_seg[j+1] = ver_seg[j-1] or ver_seg[j+1]
    if ver_seg[len(ver_seg)-1] == False: #the value of the last index is what the conditional expression evaluates to
      str_parse.pop(start_idx) #remove the conditional text from the list
  str_parse = "".join(str for str in str_parse) #fully parsed string
  return str_parse
  