
a = int(input("Qual o valor de A : "))
b = int(input("Qual o valor de B : "))
c = int(input("Qual o valor de C : "))
d = int(input("Qual o valor de D : "))
e = int(input("Qual o valor de E : "))

if a <= b <= c <= d <= e or a >= b >= c >= d >= e:
    mediana = c
elif b <= a <= c <= d <= e or b >= a >= c >= d >= e:
    mediana = c
elif a <= b <= d <= c <= e or a >= b >= d >= c >= e:
    mediana = d
elif b <= a <= d <= c <= e or b >= a >= d >= c >= e:
    mediana = d
elif a <= c <= b <= d <= e or a >= c >= b >= d >= e:
    mediana = b
elif c <= a <= b <= d <= e or c >= a >= b >= d >= e:
    mediana = b
elif a <= c <= d <= b <= e or a >= c >= d >= b >= e:
    mediana = d
elif c <= a <= d <= b <= e or c >= a >= d >= b >= e:
    mediana = d
elif a <= d <= b <= c <= e or a >= d >= b >= c >= e:
    mediana = b
elif d <= a <= b <= c <= e or d >= a >= b >= c >= e:
    mediana = b
else:
    mediana = e

print("Mediana:", mediana)
