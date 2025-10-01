loja_frutas = {
    'pera':2.40,
    'banana':3.60,
    'kiwi':4.50,
}
preco_kiwi = loja_frutas.get('kiwi',{})
print('kiwi',preco_kiwi)

loja_frutas.update({'kiwi':4.50,'mamao':10})
print(loja_frutas,'#mamao adicionado')

loja_frutas.pop('mamao')
print(loja_frutas, '#mamao removido')

for chave, valor in loja_frutas.items():
  print(f'key:{chave}: value:{valor}')