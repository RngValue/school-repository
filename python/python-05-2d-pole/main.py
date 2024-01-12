def create_2d_matrix(n: int, m: int, v: float):
  a: list[list] = []
  for _ in range(n):
    a += [[v] * m]
  return a


def print_2d_maxtrix(v: list[list[int]]):
  for i in range(len(v)):
    print(v[i])


polemhm = [[5, 2, 8], [5, 6, 7], [8, 6, 4]]

print(polemhm)
print(len(polemhm))
print(polemhm[1])
print(polemhm[1][2])

a = create_2d_matrix(2, 4, 10)
print_2d_maxtrix(a)
print_2d_maxtrix(polemhm)
