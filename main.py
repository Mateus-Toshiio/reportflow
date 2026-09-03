import csv

arquivo = "entrada/RELAÇÃO DE CONTRATOS.csv"

with open(arquivo, "r", encoding="utf-8-sig") as arquivo_csv:

    leitor = csv.reader(arquivo_csv, delimiter=";")

    linhas = list(leitor)

linha_servidor = linhas[8]
linha_setor = linhas[9]
linha_status = linhas[10]

print('SERVIDOR: ')
print(linha_servidor)

print('\nSETOR: ')
print(linha_setor)

print('\nSTATUS: ')
print(linha_status)

matricula = linha_servidor[1]
nome = linha_servidor[3]
nascimento = linha_servidor[5]
cargo = linha_servidor[7]

setor = linha_setor[10]

data_admissao = linha_status[11]

print(f'Matrícula: {matricula}')
print(f'Nome: {nome}')
print(f'Nascimento: {nascimento}')
print(f'Cargo: {cargo}')
print(f'Setor: {setor}')
print(f'Data de Admissão: {data_admissao}')

for indice, valor in enumerate(linha_servidor):
    if indice == 1 or indice == 3 or indice == 5 or indice == 7:
        print(f'{indice}° Índice {valor}')

    if valor.isnumeric() and indice == 1:
        print(f'Achamos a matrícula: {valor}')

for linha in linhas:
    if linha[1].isnumeric():
        matricula = linha[1]
        nome = linha[3]
        nascimento = linha[5]
        cargo = linha[7]
        print(f'Matrícula do servidor: {matricula}')
        print(f'Nome: {nome}')
        print(f'Nascimento: {nascimento}')
        print(f'Cargo: {cargo}')
