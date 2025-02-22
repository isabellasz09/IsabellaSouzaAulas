#del = excluir
lucro_1tri={'janeiro':1,'fevereiro':2,'março':3}
lucro_2tri={'abril':4,'maio':5,'junho':6}
del lucro_2tri['junho']
print(lucro_2tri)
#pop, removendo o conjunto chave valor de junho e atribuindo a variavel lucro_jun
lucro_1tri={'janeiro':1,'fevereiro':2,'março':3}
lucro_2tri={'abril':4,'maio':5,'junho':6}
lucro_jun=lucro_2tri.pop('junho')
print(lucro_2tri)
print(lucro_jun)
#clear, removendo todos os dados de um dicionario
lucro_1tri={'janeiro':1,'fevereiro':2,'março':3}
lucro_2tri={'abril':4,'maio':5,'junho':6}
lucro_2tri.clear()
print(lucro_2tri)