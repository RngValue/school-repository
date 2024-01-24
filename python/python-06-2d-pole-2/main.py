def soucet_poli(pole: list[list[int]]):
  soucet = 0
  for i in range(len(pole)):
    for j in range(len(pole[i])):
      soucet += pole[i][j]
  return soucet


def create_2d_matrix(n: int, m: int, v: float):
  a: list[list] = []
  for _ in range(n):
    a += [[v] * m]
  return a


def print_2d_maxtrix(v: list[list[int]]):
  for i in range(len(v)):
    print(v[i])


#Vytvořte pole (pole polí), ve kterém budou 4 pole
polepoli = [[5, 8], [8], [5, 7, 6], [15, 32]]
#Vypište pole č.3
print(polepoli[3])
#Vypište z třetího pole druhé číslo
print(polepoli[2][1])
#Sečtěte pole mezi sebou
print(soucet_poli(polepoli))

#Vytvořte dvourozměrné pole
dRPole = [[1, 2], [4, 5]]
print(dRPole)

#Vytvořte pomocí a=[[0.]*4]*2 dvourozměrné pole, kde vyměníte třetí číslo za libovolné
noveDRPole = [[0.] * 4] * 2
noveDRPole[0][2] = 69
print(noveDRPole)

#Vytvořte dvourozměrnou matici, ve které bude 5 řádků a 4 sloupce
novenoveDRPole = create_2d_matrix(5, 4, 0.)
#Ve druhém řádku a druhém sloupci změňte číslo na 4
for i in range(len(novenoveDRPole)):
  novenoveDRPole[i][1] = 4.
print_2d_maxtrix(novenoveDRPole)
