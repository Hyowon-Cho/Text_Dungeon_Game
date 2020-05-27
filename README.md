<Text_Dungeon_Game>

Welcome to Text Dungeon.

This game takes place in a three story dungeon. The user has to traverse the levels in search of the prize. 

Along the way they collect items and fight monsters. 

On each move the user has seven possible commands: left, right, up, down, grab, fight, help. 

If the input is invalid (not one of these commands,) the game will let the user know. Otherwise, the game will execute the user's command. 

The goal of the game is to collect the prize guarded by the boss monster.

---
Details
---
Behavior
  The game has three floors. Each floor is made up of five rooms, arranged in a line from left to right. A room can contain: a sword, a monster, magic stones, up-stairs, down-stairs or nothing.
At the start of the game, the user is placed in one of the rooms.
The user can try to move to the left room or right room. If there is no room in that direction, the game should report this. The user can also move upstairs or downstairs if the room contains an up-staircase or a down-staircase.
The game prints out the contents of the current room after every command.
The user can grab swords or magic stones if they walk into a room with them. The sword or stones are no longer in the room once grabbed.
Monsters guard some rooms. The user can use a sword to defeat a monster using the fight command. The sword and monster disappear after fighting. If they have no sword, the user can exit in the direction from which they came. If the user fights without a sword, they will be defeated and the game will end. If they try to walk past a monster, they will be killed and the game will end.
A sword and magic stones are required to defeat the boss monster.
--- 
Implementation Details
  The game should be implemented using lists.
    Use a list to keep track of the user's items. At the beginning of the game it should be empty. A maximum of three items can be held at once.
There should be three regular monsters placed throughout the game. These require a sword to defeat.
There should be a boss monster in the room just before the room that contains the prize. This monster requires magic stones and a sword to defeat.
The user can only go up if there is an up-staircase, and only go down if there is down-staircase.
The program should not allow the user to run past a monster, go up or down or past bounds of the game.
The game is won when the player grabs the prize.
The game is lost if the user fights a monster without a sword, fights the boss monster without a sword and stones, or tries to move past a monster.

