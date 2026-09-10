import csv

arquivo = "entrada/RELAÇÃO DE CONTRATOS.csv"

with open(arquivo, "r", encoding="utf-8-sig") as arquivo_csv:

    leitor = csv.reader(arquivo_csv, delimiter=";")

    linhas = list(leitor)

servidores = []


for indice, linha in enumerate(linhas):
    if indice + 2 < len(linhas):
        linha_setor = linhas[indice + 1]
        linha_admissao = linhas[indice + 2]
        separa_data = linha_admissao[11].split("/")
        verifica_data = separa_data[0].isnumeric() and separa_data[1].isnumeric() and separa_data[2].isnumeric()
        if linha[1].isnumeric() and linha_setor[1] == '' and linha_setor[10] != '' and verifica_data:
            matricula = linha[1]
            nome = linha[3]
            data_nascimento = linha[5]
            cargo = linha[7]
            setor = linha_setor[10]
            data_admissao = linha_admissao[11]
            servidor = {
                "matricula": matricula,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "cargo": cargo,
                "setor": setor,
                "data_admissao": data_admissao
            }
            servidores.append(servidor)

print(f'Total de servidores: {len(servidores)}')
print(servidores[0])
print(servidores[1])
print(servidores[2])

contador = 0
matriculas = set()
duplicadas = 0
for servidor in servidores:
    if servidor["matricula"] not in matriculas:
        matriculas.add(servidor["matricula"])
    else:
        duplicadas += 1
    if servidor["nome"].strip() == "":
        contador += 1

print(contador)
print(duplicadas)



    
