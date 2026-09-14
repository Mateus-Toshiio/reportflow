from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Color
from datetime import datetime

def converter_data(data):
    try:
        data_convertida = datetime.strptime(data, "%d/%m/%Y")
        return data_convertida
    except:
        return ""

def gerar_excel(servidores, arquivo_saida):
    workbook = Workbook()
    planilha = workbook.active

    planilha.title = 'Relação de Contratos'

    cabecalho = [
        "Nº",
        "MATRÍCULA",
        "NOME",
        "DATA DE NASCIMENTO",
        "CARGO",
        "SETOR",
        "DATA DE ADMISSÃO"
    ]

    planilha.append(cabecalho)

    planilha.column_dimensions["A"].width = 7.6
    planilha.column_dimensions["B"].width = 16
    planilha.column_dimensions["C"].width = 41.7
    planilha.column_dimensions["D"].width = 28
    planilha.column_dimensions["E"].width = 66.7
    planilha.column_dimensions["F"].width = 69.1
    planilha.column_dimensions["G"].width = 28

    planilha.auto_filter.ref = planilha.dimensions

    planilha.freeze_panes = "A2"

    for indice, servidor in enumerate(servidores, start=1):
        planilha.append([
            indice,
            int(servidor['matricula']),
            servidor['nome'],
            converter_data(servidor['data_nascimento']),
            servidor['cargo'],
            servidor['setor'],
            converter_data(servidor['data_admissao']),
        ])

        planilha[f"A{indice + 1}"].alignment = Alignment(horizontal="center")
        planilha[f"D{indice + 1}"].number_format = "DD/MM/YYYY"
        planilha[f"G{indice + 1}"].number_format = "DD/MM/YYYY"

    borda_fina = Side(style="thin", color="000000")
    borda_grossa = Side(style="thick", color="000000")
    ultima_linha = planilha.max_row

    for celula in planilha[1]:

        celula.font = Font(bold=True, size="14")
        celula.alignment = Alignment(horizontal="center")
        celula.border = Border(
            left=borda_grossa,
            right=borda_grossa,
            top=borda_grossa,
            bottom=borda_grossa
        )
        celula.fill = PatternFill(fgColor="BFBFBF", fill_type="solid")

    for linha in range(2, ultima_linha):
        for coluna in range(2, 7):
            planilha.cell(row=linha, column=coluna).border = Border(
                left=borda_fina,
                right=borda_fina,
                top=borda_fina,
                bottom=borda_fina
        )

    for linha in range(2, ultima_linha + 1):
        planilha[f"A{linha}"].border = Border(
            left=borda_grossa,
            right=borda_fina,
            top=borda_fina,
            bottom=borda_fina
    )

    for linha in range(2, ultima_linha + 1):
        planilha[f"G{linha}"].border = Border(
            left=borda_fina,
            right=borda_grossa,
            top=borda_fina,
            bottom=borda_fina
    )

    for coluna in range(1, 8):
        celula = planilha.cell(row=ultima_linha, column=coluna)

        celula.border = Border(
            left=borda_fina,
            right=borda_fina,
            top=borda_fina,
            bottom=borda_grossa
    )

    planilha[f"A{ultima_linha}"].border = Border(
        left=borda_grossa,
        right=borda_fina,
        top=borda_fina,
        bottom=borda_grossa
    )

    planilha[f"G{ultima_linha}"].border = Border(
        left=borda_fina,
        right=borda_grossa,
        top=borda_fina,
        bottom=borda_grossa
    )

    workbook.save(arquivo_saida)