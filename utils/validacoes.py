from datetime import datetime

def validar_data(data):
    if data == "":
        return "Ausente"
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return "Válido"
    except:
        return "Inválido"

def validar_matricula(servidores):
    matriculas = set()
    duplicadas = 0

    for servidor in servidores:
        if servidor["matricula"] not in matriculas:
            matriculas.add(servidor["matricula"])
        else:
            duplicadas += 1
    return duplicadas

def contagem_validar_datas(servidores):
    nascimento_validos = 0
    nascimento_ausentes = 0
    nascimento_invalidos = 0
    admissao_validos = 0
    admissao_ausentes = 0
    admissao_invalidos = 0

    for servidor in servidores:
        resultado_data_nascimento = validar_data(servidor["data_nascimento"])
        resultado_data_admissao = validar_data(servidor["data_admissao"])

        if resultado_data_nascimento == "Ausente":
            nascimento_ausentes += 1
        elif resultado_data_nascimento == "Inválido":
            nascimento_invalidos += 1
        elif resultado_data_nascimento == "Válido":
            nascimento_validos += 1

        if resultado_data_admissao == "Ausente":
            admissao_ausentes += 1
        elif resultado_data_admissao == "Inválido":
            admissao_invalidos += 1
        elif resultado_data_admissao == "Válido":
            admissao_validos += 1       

    return {
        "nascimento_validos": nascimento_validos,
        "nascimento_ausentes": nascimento_ausentes,
        "nascimento_invalidos": nascimento_invalidos,
        "admissao_validos": admissao_validos,
        "admissao_ausentes": admissao_ausentes,
        "admissao_invalidos": admissao_invalidos
        }
    