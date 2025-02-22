vendas_tec={'iphone':1500,'sansung galaxy':1200,'tv sansung':10000,'ps5':14300,'tablet':1720,'ipad':1200}
for chave in vendas_tec:
    print(chave)

#mostrando chave e valor com for
vendas_tec={'iphone':1500,'sansung galaxy':1200,'tv sansung':10000,'ps5':14300,'tablet':1720,'ipad':1200}
for chave in vendas_tec:
    print('O produto {} vendeu {} unidades'.format(chave,vendas_tec(chave))
      

#
vendas_tec={'iphone':1500,'sansung galaxy':1200,'tv sansung':10000,'ps5':14300,'tablet':1720,'ipad':1200}
for item in vendas_tec.items():
print(item)
#
vendas_tec={'iphone':1500,'sansung galaxy':1200,'tv sansung':10000,'ps5':14300,'tablet':1720,'ipad':1200}
for produto,vendas in vendas_tec.items():
print('{}: {} de unidades.'.format(produto,vendas))