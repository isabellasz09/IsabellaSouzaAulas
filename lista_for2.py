estoque = [1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100]
produtos=['coca cola','pepsi','guarana','skol','brahma','agua','del vale','red bull','dolly','fanta','sprit','sukita','pepsi twist']
minimo= 50
for i,qtde in enumerate(estoque):
    if qtde < minimo:
        print(produtos[i],qtde)