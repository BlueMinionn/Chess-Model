
chess_data_raw = pd.read_csv('/content/chess_games.csv', usecols=['AN','WhiteElo'])

chess_data = chess_data_raw[chess_data_raw['WhiteElo'] >2000]
del chess_data_raw
gc.collect()
chess_data = chess_data[['AN']]
chess_data = chess_data[~chess_data['AN'].str.contains('{')]
chess_data = chess_data[chess_data['AN'].str.len() > 20]

game_indices = chess_data.index

train_indices, test_indices = train_test_split(game_indices, test_size=0.2, random_state=42)

train_data = chess_data.loc[train_indices]
test_data  = chess_data.loc[test_indices]

print("Train set shape :", train_data.shape)
print("Test set shape :", train_data.shape)

print("Train set :")
print(train_data)

print("Test set :")
print(test_data)
#hi
class ChessDataset (Dataset):

  def __init__(self,games , is_train=True):
    super(ChessDataset,self).__init__()
    self.games =games
    self.is_train = is_train

  def __len__(self):
    return 706700 if self.is_train else 176676

  def __getitem__(self, index):
   game_i= np.random.randint(self.games.shape[0])
   random_game = self.games ['AN'].values [game_i]
   moves = create_move_list(random_game)
   game_state_i= np.random.randint(len(moves)-1)
   next_move = moves[game_state_i]
   moves = moves[:game_state_i]
   board = chess.Board()
   for move in moves:
    board.push_san(move)
   x = board_2_rep(board)
   y = move_2_rep(next_move,board)
   if game_state_i % 2 == 1 :
    x *= -1
   return x,y