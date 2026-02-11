"""
Módulo 4 - Dados do T2Ti ERP para IA
Vídeo 02 - Extração de Dados Reais do ERP (SQL -> Pandas)

Objetivo deste script:
- Conectar ao banco de dados do ERP
- Extrair dados financeiros reais (Contas a Receber)
- Criar o DataFrame base do módulo
- NÃO realizar limpeza ou tratamento (isso virá nos próximos vídeos)

Importante:
Este código é propositalmente simples e explícito,
para que o aluno entenda cada etapa do processo.
"""

# ======================================================
# IMPORTAÇÕES
# ======================================================

import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

# ======================================================
# CONFIGURAÇÃO DA CONEXÃO COM O BANCO DE DADOS
# ======================================================

# String de conexão com o MySQL
# Formato:
# mysql+mysqlconnector://usuario:senha@host/banco
DATABASE_URL = "mysql+pymysql://root:root@localhost/fenix"

# Criação do engine de conexão
engine = create_engine(DATABASE_URL)

# ======================================================
# DEFINIÇÃO DO SQL BASE DO MÓDULO
# ======================================================

"""
Este SQL representa o DATASET BASE do Módulo 4.

Foco:
- Contas a Receber
- Parcelas
- Cliente
- Status da Parcela
- Natureza Financeira

Neste momento:
- NÃO estamos limpando dados
- NÃO estamos corrigindo problemas
- Estamos apenas EXTRAINDO e OBSERVANDO
"""

sql = """
SELECT
    -- Identificação da parcela
    pr.id                             AS parcela_id,
    pr.numero_parcela                 AS numero_parcela,

    -- Datas importantes
    pr.data_emissao                   AS data_emissao,
    pr.data_vencimento                AS data_vencimento,
    pr.data_recebimento               AS data_recebimento,

    -- Valores financeiros da parcela
    pr.valor                          AS valor_parcela,
    pr.valor_recebido                 AS valor_recebido,
    pr.valor_juro                     AS valor_juro,
    pr.valor_multa                    AS valor_multa,
    pr.valor_desconto                 AS valor_desconto,

    -- Status da parcela
    s.situacao                        AS codigo_status,
    s.descricao                       AS descricao_status,

    -- Informações do lançamento
    lr.id                             AS lancamento_id,
    lr.valor_a_receber                AS valor_total_lancamento,
    lr.data_lancamento                AS data_lancamento,

    -- Cliente
    c.id                              AS cliente_id,
    c.nome                            AS cliente_nome,
    c.tipo                            AS cliente_tipo,
    c.limite_credito                  AS limite_credito,

    -- Natureza financeira
    nf.codigo                         AS natureza_codigo,
    nf.descricao                      AS natureza_descricao,
    nf.tipo                           AS natureza_tipo

FROM fin_parcela_receber pr

-- Relaciona parcela com o lançamento a receber
JOIN fin_lancamento_receber lr
    ON lr.id = pr.id_fin_lancamento_receber

-- Relaciona lançamento com cliente
JOIN view_pessoa_cliente c
    ON c.id = lr.id_cliente

-- Relaciona parcela com status
JOIN fin_status_parcela s
    ON s.id = pr.id_fin_status_parcela

-- Relaciona lançamento com natureza financeira
JOIN fin_natureza_financeira nf
    ON nf.id = lr.id_fin_natureza_financeira
"""

# ======================================================
# EXECUÇÃO DA CONSULTA E CARGA NO PANDAS
# ======================================================

# Executa o SQL e carrega o resultado em um DataFrame
df = pd.read_sql(sql, engine)

# ======================================================
# PRIMEIRAS INSPEÇÕES DO DATASET
# ======================================================

# Visualiza as primeiras linhas
print("\n--- HEAD ---")
print(df.head(10))

# Informações gerais do DataFrame
print("\n--- INFO ---")
print(df.info())

# Estatísticas descritivas (apenas colunas numéricas)
print("\n--- DESCRIBE ---")
print(df.describe())

# ======================================================
# OBSERVAÇÕES IMPORTANTES (DIDÁTICAS)
# ======================================================

"""
Neste ponto, é NORMAL encontrar:
- Valores nulos
- Datas vazias
- Valores recebidos diferentes do valor da parcela
- Clientes com comportamento estranho
- Status que não batem com datas

Nada disso será corrigido agora.

No próximo vídeo:
- Vamos DIAGNOSTICAR os problemas
- Identificar padrões
- Entender o que é erro, ausência legítima ou regra de negócio
"""
