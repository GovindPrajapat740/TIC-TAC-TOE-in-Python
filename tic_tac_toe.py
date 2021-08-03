from random import randint
from time import sleep

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def show_board():
  print(board[0],"|",board[1],"|",board[2],"        1   |   2  |  3")
  print("_________        ________________")
  print(board[3],"|",board[4],"|",board[5],"        4   |   5  |  6")
  print("_________        ________________")
  print(board[6],"|",board[7],"|",board[8],"        7   |   8  |  9")
  print("_________        ________________")



def check_for_win(key,p):
  if(board[0]==key and board[1]==key and board[2]==key):  #check for row 1
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[3]==key and board[4]==key and board[5]==key):  #check for row 2
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[6]==key and board[7]==key and board[8]==key):  #check for row 3
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[0]==key and board[4]==key and board[8]==key):    #check for diagonal Left to right
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[2]==key and board[4]==key and board[6]==key):    #check for diagonal right to left
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[0]==key and board[3]==key and board[6]==key):    #check for coloum 1
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[1]==key and board[4]==key and board[7]==key):    #check for coloum 1
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  elif(board[2]==key and board[5]==key and board[8]==key):    #check for coloum 1
    show_board()
    print("\n\nCongratulations,",p,"you won the game")
    return 1
  else:
    return 0
  


def check_if_full():
  if board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ':
    show_board()
    return 1
  else:
    return 0
    
    
  



  

def play(p1,p2):
  print(p1,"your key is X")
  print(p2,"your key is O")

  while True:
    p1_loop=1
    show_board()
    while p1_loop:
      print("\n"*2,p1," this is your turn, enter your position from : 1-9")
      position_p1=int(input())
      if position_p1 in range(1,10):
        if board[position_p1-1]==' ':
          board[position_p1-1]='X'
          p1_loop=0
          if check_for_win('X',p1):
            return
          if check_if_full():
            print("\n\nthe match is DRAW,  THANKYOU","\n"*2)
            return
          
        else:
          print("this position is already filled, please select an empty position")
          continue
      else:
        print("invalid choice, your choice must be in the range of 1-9")
        continue
    show_board()
    p2_loop=1
    while p2_loop:
      print("\n"*2,p2," this is your turn, enter your position from : 1-9")
      position_p2=int(input())
      if position_p2 in range(1,10):
        if board[position_p2-1]==' ':
          board[position_p2-1]='O'  
          p2_loop=0
          if check_for_win('O',p1):
            return
          if check_if_full():
            print("the match is DRAW,  THANKYOU","\n"*2)
            return
        else:
          print("this position is already filled, please select an empty position")
          continue
      else:
        print("invalid choice, your choice must be in the range of 1-9")
        continue
    

    
  


def start():
  player_1=input("enter the name of player_1")
  player_2=input("enter the name of player_2")
  
  print("\n"*2,"initially your game board looks like this:")
  show_board()
  print("\n\nlets do the toss:\
         \n1. if result is HEAD (1)",player_1," will have the first turn\
         \n2.if result is TAIL (2)",player_2," will have the first turn",2*"\n",\
         "Are you ready for TOSS:  y/n")
  while True:
    toss_or_not=input()
    if toss_or_not==('y'or'Y'):
      toss_result= randint(1,2)
      if toss_result == 1:
        print("\n\nresult is HEAD ",player_1," won the toss")
        play(player_1,player_2)
        return 1
        
      else:
        print("\n\nresult is TAIL ",player_2," won the toss")
        play(player_1,player_2)
        break
        
    
    elif toss_or_not==('n'or'N'):
      print("It seems you did not like the game, Its ok, GOOD BYE!")
      print("hope to see you again, THANKYOU")
      return 0
    else:
      print("wrong choice, enter a valid key")
      continue
  
    
          
  
  
  




         #the execution of the code starts from here

print("           --------------------------")
print("     ----| WELCOME TO THE TIC-TAC-TOE |----")
print("           --------------------------")

print("Please read the following instructions carefully :","\n"*2)
print("1.first turn would be decided by toss \n\
2.to win the game a player must occupy all the three adjacent places of a ROW/COLOUMN/DIAGONAL\n\
3.if any of the player is not able to occupy a ROW/COLOUMN/DIAGONAL and all places are full the game will be over\n\
4.In third case the game would be said as TIE or DRAW ")



while True:
  print("ARE YOU READY TO START THE GAME: Y/N ")
  start_game=input()
  
  if start_game == ('y' or 'Y'):
    while True:
      status = start()
      if status==0:
        break
      print("\n"*3)
      print("             ----------------")
      print("        ----|the game is over|----")
      print("             ----------------")
      print("\n"*3)
      break
      
      
    
  elif start_game == ('n' or 'N'):
    print("OK, see you next time.  Thankyou for coming")
    break 
  else:
    print("bad choice, enter your choice again")
    continue
  if status==0: 
        break
  break
sleep(10)
  
  

  
