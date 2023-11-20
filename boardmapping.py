letter_2_num= {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
num_2_letter= {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}

def board_2_rep(board):
 pieces = ['p','r','n','b','q','k']
 layers= []
 for piece in pieces:
  layers.append(create_rep_layer(board,piece))
 board_rep= np.stack(layers)
 return board_rep

def create_rep_layer(board,type):
  s=str(board)
  s= re.sub (f'[^{type}{type.upper()} \n]', '.',s)
  s= re.sub (f'{type}', '-1',s)
  s= re.sub (f'{type.upper()}','1',s)
  s= re.sub (f'\.','0',s)


  board_mat = []
  for row in s.split('\n'):
   row = row.split(' ')
   row = [int(x) for x in row]
   board_mat.append(row)

  return np.array(board_mat)

def move_2_rep(move,board):

  board.push_san(move).uci()
  move = str (board.pop())

  from_output_layer = np.zeros ((8,8))
  from_row = 8 - int(move[1])
  from_column = letter_2_num[move[0]]
  from_output_layer[from_row,from_column] = 1

  to_output_layer = np.zeros((8,8))
  to_row = 8 - int(move[1])
  to_column = letter_2_num[move[0]]
  to_output_layer[to_row,to_column] = 1

  return np.stack ([from_output_layer, to_output_layer])

def create_move_list(s):
  return re.sub('\d*\. ','',s).split(' ')[:-1] 