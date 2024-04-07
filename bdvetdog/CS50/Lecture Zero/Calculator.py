'''x = float(input("What's X?\nAnswer: "))
y = float(input("What's Y?\nAnswer: "))

#z = round(x/y, 2) arredonda o resultado em duas casas decimais
z = x/y

#print(f"{z:,}") # podes formatar os números floats com pontos e vírgulas dessa maneira
print(f"{z:.2f}")'''
def main():
    x = int(input("What's X? "))
    print("x squared is", square(x))

def square(n):
    #return n * n
    #return n ** 2 #essa sintaxe também é para potência
    return pow(n, 2) #essa também é para potência

main()