numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
kolvo = len(numbers)
prop_simb = numbers.index(None)
summa = sum(numbers[:prop_simb])+sum(numbers[prop_simb+1:])
srednee = summa / kolvo
numbers[numbers.index(None)] = srednee
print("Измененный список:", numbers)
