#Declarando uma lista

lista = [1,2,3,4,5,6,7,8,9,0,"teste",True,False]

print("lista", lista)

print(lista[0])  ##Printando apenas o indice zero da lista

print(lista[1:7]) ## printando do indice 1 até o 7  

##método append, adiciona um elemento no final da lista

lista.append("rs")
print(lista)

#Método index, encontra o local que o elemento que estou procurando, está

indice = lista.index("rs")

print(indice)

##Método pop --> remove o elemento da lista no indice indicado

elemento_removido = lista.pop(3)
print(elemento_removido)

##Método remove --> rmeove o primeiro elemento encontrado com o valor solicitado

lista.remove(2)
print(lista)
