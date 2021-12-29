'''
def busca_binaria(list, item):
   primeiro = 0
   ultimo = len(list)-1
   encontrado = False
	
   while (primeiro <= ultimo) and not encontrado:
      meio = (primeiro + ultimo)//2
      if list[meio] == item:
         encontrado = True
      else:
         if item < list[meio]:
            ultimo = meio - 1
         else:
            primeiro = meio + 1
	
   return encontrado
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(busca_binaria(testlist, 3))
print(busca_binaria(testlist, 13))
'''

'''
def busca_binaria_recursiva(list, item):
   if len(list) == 0:
      return False
   else:
      meio = len(list)//2
      if list[meio] == item:
         return True
      else:
         if item < list[meio]:
            return busca_binaria_recursiva(list[:meio],item)
         else:
            return busca_binaria_recursiva(list[meio+1:],item)
         return None
   
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
testes = [80,50]
for t in testes:
   pos = busca_binaria_recursiva(testlist,t)
   if pos is None:
      print("Não achei",t)
   else:
      print("Achei", t)
'''

def busca_binaria(lista, x):
   primeiro = 0
   ultimo = len(lista)-1

   while primeiro <= ultimo:
      meio = (primeiro + ultimo) //2
      if lista[meio] == x:
         return meio
      else:
         if x < lista[meio]:
            ultimo = meio - 1
         else:
            primeiro = meio + 1
   return -1



