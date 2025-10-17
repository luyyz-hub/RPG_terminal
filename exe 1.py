players = {
    '1': {
        'nome': 'Nilson',
        'idade': 24,
        'ryos': 320.50,
        'classe': 'Mago',
        'familia': 'Loki',
        'habilidades': {
            'ataque': 10,
            'defesa': 5,
            'vida': 10
        },
        'nivel': 100,
        'xp': 0,
        'equipamentos': [2],
        'dungeon':1
    },
    '2': {
        'nome': 'Luiz',
        'idade': 15,
        'ryos': 320.50,
        'classe': 'Mago',
        'familia': 'Mongólis',
        'habilidades': {
            'ataque': 12,
            'defesa': 5,
            'vida': 8
        },
        'nivel': 1,
        'xp': 0,
        'equipamentos': [0]
    }
}

equipamentos = {
    '1': {
        'nome': 'Espada de madeira',
        'classe': 'Guerreiro',
        'habilidades': {
            'ataque': 1,
            'defesa': 1,
            'vida': 0}
    },
    '2':{
        'nome': 'livro velho',
        'classe': 'mago',
        'habilidades': {
            'ataque': 1,
            'defesa': 0,
            'vida': 1,}
},
    '3':{
        'nome': 'arco de madeira',
        'classe': 'arqueiro',
        'habilidades': {
            'ataque': 2,
            'defesa': 0,
            'vida': 0,}
}
}
monstros = {
     1:{'nome':'Rato',
       'habilidade':{
           'ataque':1,
           'defesa':0,
           'vida':1,}
      },
      2:{'nome':'Formiga',
       'habilidade':{
           'ataque':2,
           'defesa':2,
           'vida':1,}
      },
      3:{'nome':'Coelho',
       'habilidade':{
           'ataque':4,
           'defesa':3,
           'vida':1,}
      }
},


def iniciar():
    print('Bem vindo ao RPG terminal!')
    id = str(input('qual seu id?'))
    personagens = players[id]
    print(personagens['nome'])

    print('menu\n1-dungeon')

    escolha = input('escolha uma opção:')
    if escolha == '1':
      print('Você entrou na dungeon')
      explorarDungeon(personagens)

def explorarDungeon(players):
  print('você está explorando a Dungeon no andar:',
        players.get('dungeon'))
  ativar_armas(players)
  luta(players,monstros.get(players['dungeon']))

def ativar_armas(players):
  if len(players.get('equipamentos'))== 0:
    print('você não tem equipamentos no seu inventario')
    pass
  for i in players.get('equipamentos'):
    if equipamentos.get(str(i))== None:
      print('você não tem equipamentos validos no seu inventario')
    elif players.get('classe') == equimentos.get(str(i)).get('classe'):
      print(f'seu equipamento é um(a){equipamentos.get(str(i)).get("nome")}')
  for j, k in equipamentos.get(str(i)).get('habilidades').itens():
    players.get('habilidades')[j] += k

  else:
      print('voce nao tem equipamentos para sua classe')


iniciar()

