# TODO Найдите количество книг, которое можно разместить на дискете
simb = 25
strok = 50
ctr = 100
ves_one_simb = 4
V_Mb = 1.44
V_B = 1.44*1024*1024
ves_one_book = ves_one_simb*ctr*strok*simb
kolvo = V_B // ves_one_book

print("Количество книг, помещающихся на дискету:", round(kolvo))
