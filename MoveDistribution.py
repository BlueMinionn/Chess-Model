
def distribution_over_moves (vals):
  probs = torch.tensor(vals, dtype=torch.float32)
  probs = torch.exp(probs)
  probs = probs / probs.sum()
  probs = probs ** 3
  probs = probs / probs.sum()
  return probs.detach().cpu().numpy()