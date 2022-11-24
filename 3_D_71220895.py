riski = int(input("Masukkan tahun: "))

if riski % 400 == 0:
    print("{} merupakan tahun kabisat".format(riski))
elif riski % 100 == 0:
    print("{} bukan tahun kabisat".format (riski))
elif riski % 4 == 0:
    print("{} merupakan tahun kabisat".format(riski))
else:
    print("{} bukan tahun kabisat".format(riski))