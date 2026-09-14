from utils.validacoes import contagem_validar_datas, validar_matricula
from processadores.contratos import processar_contratos
from utils.validacoes import validar_matricula

arquivo = "entrada/RELAÇÃO DE CONTRATOS.csv"

servidores = processar_contratos(arquivo)

duplicadas = validar_matricula(servidores)

resultado_datas = contagem_validar_datas(servidores)



    
