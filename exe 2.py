loja_carro ={
    'civic':{
        'valor':220,
        'cor':'azul',
    },
    'bmw':{
         'valor':330,
          'cor':'verde',
    },
    'fusca':{
         'valor':555,
        'cor':'roxo',
    }
}
preco_fusca = loja_carro.get('fusca',{})
print('fusca',preco_fusca)

for k,v in loja_carro.items():
      loja_carro.get(k)['valor']*=1.25
print(loja_carro)