vendas=[100,50,80,190,200,210,45,37,99,105,130,111,44,24,67,93,157,25]
meta= 100
bateu_meta=0
for venda in vendas:
    if venda >= meta:
        bateu_meta +=1
qtde_funcionario= len(vendas)
print('O porcentual de pessoas que bateu a meta foi de {:.1%}'.format(bateu_meta/qtde_funcionario))
