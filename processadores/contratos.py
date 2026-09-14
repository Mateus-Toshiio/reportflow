import csv

from utils.validacoes import validar_data


def processar_contratos(arquivo):
    servidores = []

    with open(arquivo, "r", encoding="utf-8-sig") as arquivo_csv:

        leitor = csv.reader(arquivo_csv, delimiter=";")

        linhas = list(leitor)

    for indice, linha in enumerate(linhas):
        if indice + 2 < len(linhas):
            linha_setor = linhas[indice + 1]
            linha_admissao = linhas[indice + 2]
            if linha[1].isnumeric() and linha_setor[1] == '' and linha_setor[10] != '' and validar_data(linha_admissao[11]) == 'Válido':
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

    return servidores