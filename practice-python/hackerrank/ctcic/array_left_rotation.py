def array_left_rotation(arr, n, k):
  return arr[k:] + arr[:k]

def array_right_rotation(arr, n, k):
  return arr[-k:] + arr[:-k]