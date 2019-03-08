dados = {
'Rod': '1234',
'Gui': '4321',
'Guga': '1111',
'Kerley': '2222',
'Gaspar': '3333'
}

def get_verify(chave, valor):
    if chave in dados:
        if dados[chave] == valor:
            return True
    else:
        return False



