def eh_par():
    for n in list(range(1, 10)):
        if n % 2 == 0:
            print(f"{n} é par.")
        else:
            print(f"{n} é ímpar.")

par = eh_par()
print(par)