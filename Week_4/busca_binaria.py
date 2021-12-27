def busca_binaria(seq, x):
   ''' (list, float) -> bool
        retorna a posicao em que x ocorre na lista ordenada,
        ou None caso contrario, usando o algoritmo de busca binaria.
        '''

   m = len(lista)/2

   for n in lista[m]:
      if n == lista[m]:
         return
      elif n > lista[m]:
         
   return None


# escreva alguns testes da funcao busca_binaria
seq = [4, 10, 80, 90, 91, 99, 100, 101]
testes = [80, 50]

for t in testes:
    pos = busca_binaria(seq, t)
   if pos is None:
      print("Nao achei ", t)
   else:
      print("Achei ", t)


