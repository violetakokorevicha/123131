import math
atalgojums = float(input("Iavadi algus:"))
klients = int(input("Ievadi klientu sk:"))
pelna = float(input("Īevadi nopelnīto uznemumu naudu:"))
def function(atalgojums):
  if klients > 5 and pelna > 1000:
    atalgojums = atalgojums + atalgojums * 0.25
    print("Stradnieka atalgojums ar bonusus ir:",atalgojums)
  else:
    atalgojums == atalgojums
    print("Stradnieka atalgojums ,ez bonusa ir:",atalgojums)
function(atalgojums)

a1 = int(input("Ievadi a1:"))
b1 = int(input("Ievadi b1:"))
c1 = int(input("Ievadi c1:"))
def function_rtu():
    if a1 + b1 + c1 == 180:
      print("Trijsturis ir derīgs:")
    else:
      print("Trijsturis nav derīgs")
    if a1 == 90 or b1 == 90 or c1 == 90:
      print("Taisnlenka trijsturis")
    elif a1 > 90 or b1 > 90 or c1 > 90:
      print("Platļeņķa trijsturis")
    else:
      print("Šaurļenka trijsturis")
function_rtu()


st = int(input("Skaits diapozona:"))
beg = int(input("Skaits diapozona beigam(nav diapozona):"))
def function_LU():
   for i in range(st, beg):
     print(math.factorial(i))
function_LU()
  
    