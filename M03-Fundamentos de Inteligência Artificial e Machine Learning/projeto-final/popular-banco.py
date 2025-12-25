import pymysql
import random
from datetime import datetime, timedelta

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Configuração da conexão
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'fenix',
    'port': 3306
}

def popular_banco():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # 1. Mapeamento fiel à sua tabela fin_status_parcela
    status_erp = {
        'ABERTO': 1,
        'QUITADO': 2,
        'QUITADO_PARCIAL': 3,
        'VENCIDO': 4,
        'RENEGOCIADO': 5
    }

    # 2. Obter clientes existentes
    cursor.execute("SELECT id, limite_credito FROM cliente")
    clientes = cursor.fetchall()
    
    if not clientes:
        print("❌ Nenhum cliente encontrado. Cadastre clientes primeiro.")
        return

    print(f"🚀 Populando banco com IDs reais: {status_erp}")

    data_atual = datetime.now()

    for i in range(500):
        id_cliente, limite = random.choice(clientes)
        qtd_parcelas = random.randint(1, 10)
        valor_total = float(limite) * random.uniform(0.1, 0.8)
        valor_parcela = valor_total / qtd_parcelas
        
        # Inserir Lançamento
        sql_lancamento = "INSERT INTO fin_lancamento_receber (id_cliente, id_fin_natureza_financeira, id_fin_documento_origem, id_banco_conta_caixa, quantidade_parcela, valor_a_receber, data_lancamento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_lancamento, (id_cliente, 1, 1, 1, qtd_parcelas, valor_total, data_atual))
        id_lancamento = cursor.lastrowid

        for n in range(1, qtd_parcelas + 1):
            # Simulando datas para criar passado (histórico) e futuro (previsão)
            # Algumas parcelas vencem 60 dias atrás, outras 60 dias à frente
            dias_deslocamento = (n * 30) - 60 
            vencimento = data_atual + timedelta(days=dias_deslocamento)
            
            sorteio = random.random()
            
            # LÓGICA DE STATUS
            if vencimento < data_atual:
                # PASSADO: Definimos entre Quitado ou Vencido para o modelo aprender
                if limite > 3000: # Clientes com limite alto pagam melhor no nosso simulador
                    id_status = status_erp['QUITADO'] if sorteio < 0.85 else status_erp['VENCIDO']
                else:
                    id_status = status_erp['QUITADO'] if sorteio < 0.50 else status_erp['VENCIDO']
                
                valor_pago = valor_parcela if id_status == status_erp['QUITADO'] else 0
                data_receb = vencimento if id_status == status_erp['QUITADO'] else None
            else:
                # FUTURO: O que o modelo vai tentar prever
                id_status = status_erp['ABERTO']
                valor_pago = 0
                data_receb = None

            sql_parcela = """
            INSERT INTO fin_parcela_receber 
            (id_fin_lancamento_receber, numero_parcela, valor, data_emissao, data_vencimento, 
            data_recebimento, valor_recebido, id_fin_status_parcela) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_parcela, (
                id_lancamento, n, valor_parcela, data_atual - timedelta(days=60), 
                vencimento, data_receb, valor_pago, id_status
            ))

    conn.commit()
    print(f"✨ Sucesso! 500 lançamentos inseridos com status vinculados corretamente.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    popular_banco()