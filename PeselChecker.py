#Pesel Checker 0.1 Autor: Pawel Furman CC0 1.0
#Pesel input
num = input ("Podaj pesel: ")
#PeselNo
num_str = str(num)
cyfra1 = num_str[0]
cyfra2 = num_str[1]
cyfra3 = num_str[2]
cyfra4 = num_str[3]
cyfra5 = num_str[4]
cyfra6 = num_str[5]
cyfra7 = num_str[6]
cyfra8 = num_str[7]
cyfra9 = num_str[8]
cyfra10 = num_str[9]
cyfra11 = num_str[10]
#convertToString
liczba1 = int(cyfra1)
liczba2 = int(cyfra2)
liczba3 = int(cyfra3)
liczba4 = int(cyfra4)
liczba5 = int(cyfra5)
liczba6 = int(cyfra6)
liczba7 = int(cyfra7)
liczba8 = int(cyfra8)
liczba9 = int(cyfra9)
liczba10 = int(cyfra10)
liczba11 = int(cyfra11)
#controlNumberMultiplication
mnoznik1 = liczba1*1
mnoznik2 = liczba2*3
mnoznik3 = liczba3*7
mnoznik4 = liczba4*9
mnoznik5 = liczba5*1
mnoznik6 = liczba6*3
mnoznik7 = liczba7*7
mnoznik8 = liczba8*9
mnoznik9 = liczba9*1
mnoznik10 = liczba10*3
#pickingTheLastDigit
ostCyfra1 = int(str(mnoznik1)[-1])
ostCyfra2 = int(str(mnoznik2)[-1])
ostCyfra3 = int(str(mnoznik3)[-1])
ostCyfra4 = int(str(mnoznik4)[-1])
ostCyfra5 = int(str(mnoznik5)[-1])
ostCyfra6 = int(str(mnoznik6)[-1])
ostCyfra7 = int(str(mnoznik7)[-1])
ostCyfra8 = int(str(mnoznik8)[-1])
ostCyfra9 = int(str(mnoznik9)[-1])
ostCyfra10 = int(str(mnoznik10)[-1])
#controlNumber
ctrlNo = ostCyfra1+ostCyfra2+ostCyfra3+ostCyfra4+ostCyfra5+ostCyfra6+ostCyfra7+ostCyfra8+ostCyfra9+ostCyfra10
#controlDigit
ctrlDig = int(str(ctrlNo)[-1])
#output
print("Podałeś Pesel:", num)
if ctrlDig == 10 - liczba11:
  print("Pesel jest poprawny!")
elif ctrlDig != liczba11:
  print("Do urzędu wyjaśnić sprawę!")