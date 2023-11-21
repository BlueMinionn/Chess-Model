
def choose_move (board, color):

  legal_moves = list(board.legal_moves)


  x, _ = torch.Tensor (board_2_rep(board)),float()
  if color == chess.BLACK:
    x *= -1
  x = x.unsqueeze(0)
  move = model_0(x)

  vals = []
  fromz= []
  for move_l in legal_moves:
    move__= move_l.uci()
    from_= str(move__)
    from_ = from_[:2]
    fromz.append(from_)

  froms = list(set(fromz))

  for from_ in froms:
    val = move[0,0,:,:]  [ 8 - int(from_[1]) , letter_2_num[from_[0]]]
    vals.append(val)

  probs = distribution_over_moves(vals)


  choosen_from = str(np.random.choice(froms, size=1, p=probs)[0])[:2]
  vals = []
  for legal_move in legal_moves:
    from_ = str(legal_move)[:2]
    if from_ == choosen_from:
      to = str(legal_move) [2:]
      val = move[0,1,:,:] [8 - int(to[1]), letter_2_num[to[0]]]
      vals.append(val)
    else:
      vals.append(0)

  choosen_move = legal_moves[int(vals.index(max(vals)))]
  return choosen_move