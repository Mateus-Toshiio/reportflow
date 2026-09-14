from utils.validacoes import contagem_validar_datas, validar_matricula
from processadores.contratos import processar_contratos
from utils.validacoes import validar_matricula
from processadores.excel import gerar_excel

arquivo = "entrada/RELAÇÃO DE CONTRATOS.csv"

servidores = processar_contratos(arquivo)

gerar_excel(servidores, "saida/Relação de contratos limpo.xlsx")

duplicadas = validar_matricula(servidores)

resultado_datas = contagem_validar_datas(servidores)



    
