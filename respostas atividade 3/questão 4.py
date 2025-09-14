#Gerador de tabuada 

numero_tabuada = int(input("Digite o número da tabuada: "))

print(f"Tabuada do {numero_tabuada}")
for j in range (1,11):
     print(f"{numero_tabuada} x {j} = {numero_tabuada*j}")

'''
^ Esse codigo permite ao usuario puxar a tabuada do 1 ao 10 de qualquer numero inteiro que ele quiser
e assim fica bem otimizado sem precisar de ifs nem while, assim permitindo ao usuario nao fritar o pc 
enquanto o codigo roda infinitamente
'''
