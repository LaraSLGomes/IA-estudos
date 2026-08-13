print("hello world") 

idade :int = 21

print(idade)

animais = ["gato", "cachorro"] #homogeneas

coisas = [2.3, 4, "casa"] #heterogeneas

print(type(coisas)) 

tp = ("casa", 4, 6.5) #imutavel 

print(type(tp))

dic = {"animal": "gato", "idade": 4} #pares (chave:valor)

print(type(dic))

print(animais[0])

print(dic["animal"])

if idade > 80:

    print("idade maior que 80")
else:
    print("idade menor que 80")

    for a in nomes:
        print(a)

def subprograma():
    print("oi")
subprograma()