def get_middle(s):
  return string[int(len(string) / 2)] if len(string) % 2 != 0 else string[int(len(string) / 2) - 1: int(len(string) / 2) + 1]
