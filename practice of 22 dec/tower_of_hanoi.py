def tower_of_hanoi(n,A,B,C):
    if n== 1:
        print( f" {n} {A} to {C}")
    else:

     tower_of_hanoi(n-1,A,C,B)
     print(f"{n} {A} to {C}")

     tower_of_hanoi(n-1 , B,A,C)


n =3
# a =""
# b = ""
# c =""
tower_of_hanoi(n,"a","b","c")
