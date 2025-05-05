import pymysql
import json

# Conexão com PyMySQL
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='fenix',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

tabelas_financeiras = [
    'fin_status_parcela',
    'fin_tipo_pagamento',
    'fin_tipo_recebimento',
    'fin_documento_origem',
    'fin_cheque_emitido',
    'fin_cheque_recebido',
    'fin_configuracao_boleto',
    'fin_extrato_conta_banco',
    'fin_fechamento_caixa_banco',
    'fin_lancamento_pagar',
    'fin_lancamento_receber',
    'fin_parcela_pagar',
    'fin_parcela_receber'
]

def obter_dicionario_tabela(cursor, tabela):
    try:
        cursor.execute(f"SHOW FULL COLUMNS FROM {tabela}")
        colunas = cursor.fetchall()

        cursor.execute(f"""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = DATABASE()
            AND TABLE_NAME = %s
            AND CONSTRAINT_NAME = 'PRIMARY'
        """, (tabela,))
        chaves_primarias = {linha['COLUMN_NAME'] for linha in cursor.fetchall()}

        dicionario = []
        for coluna in colunas:
            dicionario.append({
                'coluna': coluna['Field'],
                'tipo': coluna['Type'],
                'chave_primaria': coluna['Field'] in chaves_primarias,
                'comentario': coluna['Comment']
            })
        return dicionario

    except Exception as e:
        print(f"Erro na tabela {tabela}: {e}")
        return []

def gerar_dicionario():
    try:
        with conexao.cursor() as cursor:
            dicionario_geral = {}

            for tabela in tabelas_financeiras:
                print(f"Lendo estrutura da tabela: {tabela}")
                dicionario_geral[tabela] = obter_dicionario_tabela(cursor, tabela)

            with open('dicionario_dados_financeiro.json', 'w', encoding='utf-8') as f:
                json.dump(dicionario_geral, f, indent=4, ensure_ascii=False)

            print("Dicionário salvo em 'dicionario_dados_financeiro.json'.")

    finally:
        conexao.close()

if __name__ == "__main__":
    gerar_dicionario()
