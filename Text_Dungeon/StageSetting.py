# Room Setting

user_room = 4
user_floor = floor_1
game_over = False
user_items = []
last_command = ""

while (game_over==False): 
  user_input = (input(" what would you like to do? "))
  
  if user_input == "left":
    if user_room == 0:
      print("there are no more rooms")
    elif user_floor[user_room] == "monster" and last_command == "left" :
      print("you lost")
      game_over = True
    else:
      user_room = user_room - 1
     
    
  elif user_input == "right":
    if user_room == 4:
      print("there are no more rooms")
    elif user_floor[user_room] == "monster" and last_command == "right" :
      print("you lose!")
      game_over = True 
    else:
      user_room = user_room + 1 

    
  elif user_input == "up":
    if user_floor[user_room] == "upstairs":
      if user_floor == floor_1:
        user_floor = floor_2
      else:
        user_floor = floor_3 
    else:
      print("there is no staircase to go upstairs")
        
  
  elif user_input == "down":
    if user_floor[user_room] == "downstairs":
      if user_floor == floor_3:
        user_floor = floor_2
      else: 
        user_floor = floor_1
    else:
      print("there is no staircase to go downstairs")
  
  elif user_input == "grab":
    if len(user_items) < 3:
      if user_floor[user_room] == "sword" or user_floor[user_room] == "magic stone":
        user_items.append(user_floor[user_room])
        user_floor[user_room] = "nothing"
      elif user_floor[user_room] == "prize":
        print("you won the game!")
        game_over = True
      else:
        print("you can't grab")
    else:
      print("you can't grab more than 3 items")
  
  elif user_input == "fight":
    if user_floor[user_room] == "monster":
      if "sword" in user_items:
        user_floor[user_room] = "nothing"
        user_items.remove("sword")
      else: 
        print("you lost ")
        game_over = True 
    if user_floor[user_room] == "boss monster":
      if "sword" in user_items and "magic stone" in user_items:
        user_floor[user_room] = "nothing"
        user_items.remove("sword")
        user_items.remove("magic stone")
      else: 
        print("you lost")
        game_over = True 
      
      
       
  print ("this room has: " + user_floor[user_room])
  
  last_command = user_input 
    
