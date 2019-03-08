academico = {
"Rod": [['Matematica', '8', '7', '6'], ['L.P', '6.5', '6.0', '6.0'], ['Historia', '8.5', '9.0', '10']],
"Gui": [['Matematica', '6', '6', '6'], ['L.P', '4.5', '6.0', '5.0'], ['Historia', '8.5', '8', '8.0']],
"Guga": [['Matematica', '9', '9', '9'], ['L.P', '6.0', '6.0', '6.0'], ['Historia', '8.5', '8', '8.0']],
"Kerley": [['Matematica', '10', '10', '10'], ['L.P', '7', '7', '7'], ['Historia', '6.0', '6.0', '6.0']],
"Gaspar": [['Matematica', '5', '5', '5'], ['L.P', '9', '9', '9'], ['Historia', '8.5', '8', '8.0']]
}

def get_notas(chave):
    lista1 = []
    lista2 = []
    lista3 = []
    lista1.append(academico[chave][0][1:])
    lista2.append(academico[chave][1][1:])
    lista3.append(academico[chave][2][1:])
    lista = [lista1, lista2, lista3]
    return lista

def get_materias(chave):
    lista = []
    lista.append(academico[chave][0][0])
    lista.append(academico[chave][1][0])
    lista.append(academico[chave][2][0])
    return lista