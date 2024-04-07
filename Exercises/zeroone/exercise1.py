# como funciona a equação de fibonacci?
# a equação de fibonacci funciona com a soma de dois números, e após somado
# ele será somado com o valor anterior
# ou seja, começamos com 0 e 1, 0+1 = 2, soma esse dois, com o 1, logo 2+1 = 3, depois 3 + 2 = 5, depois 5 + 3 = 8 e assim
# por diante
# a formula de fibonacci é "F = F(n-1) + F(F+2)" 
# tenho que arranjar uma forma de fazer essa formula funcionar

fibonacci_number = 13
fibonacci = 0
while fibonacci != fibonacci_number:
    fibonacci = fibonacci + (fibonacci+1)
    print(fibonacci)
    if fibonacci > fibonacci_number:
        break