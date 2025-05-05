from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError
import json
from datetime import datetime
import sys
import os

def get_db_connection():
    """Estabelece conexão com o banco de dados usando SQLAlchemy"""
    try:
        print("\nConfigurando conexão com o banco de dados...")
        
        # String de conexão - altere conforme necessário
        db_url = "mysql+mysqlconnector://root:root@localhost/fenix"
        
        print(f"URL de conexão: {db_url}")
        engine = create_engine(db_url, echo=False)  # Altere echo=True para ver o SQL gerado
        
        print("Testando conexão...")
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))  # Teste simples
            print("✓ Conexão estabelecida com sucesso!")
            return engine
    except SQLAlchemyError as err:
        print(f"\n× ERRO DE CONEXÃO: {str(err.__cause__)}", file=sys.stderr)
        print("Verifique:\n- Servidor MySQL está rodando?\n- Credenciais corretas?\n- Banco 'fenix' existe?")
        return None
    except Exception as e:
        print(f"\n× ERRO INESPERADO: {str(e)}", file=sys.stderr)
        return None

def get_table_metadata(engine, table_name):
    """Obtém metadados completos de uma tabela"""
    inspector = inspect(engine)
    try:
        # Obtém comentário da tabela
        table_comment = engine.dialect.get_table_comment(engine, table_name)['text']
        
        # Obtém colunas com detalhes
        columns = []
        for column in inspector.get_columns(table_name):
            col_info = {
                'name': column['name'],
                'type': str(column['type']),
                'nullable': column['nullable'],
                'default': str(column['default']) if column['default'] is not None else None,
                'comment': column.get('comment'),
                'primary_key': column['primary_key']
            }
            columns.append(col_info)
        
        # Obtém chaves estrangeiras
        foreign_keys = []
        for fk in inspector.get_foreign_keys(table_name):
            fk_info = {
                'name': fk['name'],
                'constrained_columns': fk['constrained_columns'],
                'referred_table': fk['referred_table'],
                'referred_columns': fk['referred_columns']
            }
            foreign_keys.append(fk_info)
        
        return {
            'description': table_comment,
            'columns': columns,
            'foreign_keys': foreign_keys
        }
    except SQLAlchemyError as e:
        print(f"Erro ao obter metadados da tabela {table_name}: {str(e)}", file=sys.stderr)
        return None

def get_financial_tables(engine):
    """Lista tabelas do módulo financeiro com verificação"""
    inspector = inspect(engine)
    all_tables = inspector.get_table_names()
    
    financial_tables = [
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
    
    # Verifica quais tabelas existem no banco
    existing_tables = [t for t in financial_tables if t in all_tables]
    
    print(f"\nTabelas encontradas no banco: {len(existing_tables)}/{len(financial_tables)}")
    for t in financial_tables:
        status = "✓" if t in existing_tables else "×"
        print(f" {status} {t}")
    
    return existing_tables

def generate_knowledge_base(engine):
    """Gera o dicionário de conhecimento completo"""
    print("\nIniciando geração do banco de conhecimento...")
    
    knowledge_base = {
        'metadata': {
            'system': 'ERP Fênix',
            'module': 'Financeiro',
            'generated_at': datetime.now().isoformat(),
            'database': engine.url.database,
            'tables_count': 0,
            'version': '1.0'
        },
        'tables': {}
    }
    
    financial_tables = get_financial_tables(engine)
    
    for table in financial_tables:
        print(f"\nProcessando tabela: {table}")
        metadata = get_table_metadata(engine, table)
        
        if metadata:
            knowledge_base['tables'][table] = metadata
            print(f" ✓ {len(metadata['columns'])} colunas processadas")
            if metadata['foreign_keys']:
                print(f"   {len(metadata['foreign_keys'])} relacionamentos encontrados")
        else:
            print(f" × Falha ao processar tabela {table}")
    
    knowledge_base['metadata']['tables_count'] = len(knowledge_base['tables'])
    return knowledge_base

def save_knowledge_base(data, filename):
    """Salva o banco de conhecimento em arquivo JSON"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        file_path = os.path.abspath(filename)
        print(f"\nArquivo gerado com sucesso: {file_path}")
        return True
    except Exception as e:
        print(f"\n× ERRO AO SALVAR ARQUIVO: {str(e)}", file=sys.stderr)
        return False

def main():
    print("=== GERADOR DE BANCO DE CONHECIMENTO ===")
    print("Versão SQLAlchemy 1.0\n")
    
    # 1. Conectar ao banco
    engine = get_db_connection()
    if not engine:
        print("\nFalha na conexão. Verifique os erros acima.")
        return
    
    try:
        # 2. Gerar conhecimento
        knowledge_base = generate_knowledge_base(engine)
        
        if not knowledge_base['tables']:
            print("\nNenhuma tabela foi processada com sucesso!")
            return
        
        # 3. Salvar resultados
        output_file = "banco_conhecimento_financeiro.json"
        print(f"\nSalvando resultados em {output_file}...")
        
        if save_knowledge_base(knowledge_base, output_file):
            print("\nProcesso concluído com sucesso!")
        else:
            print("\nProcesso concluído com erros ao salvar.")
    
    except Exception as e:
        print(f"\n× ERRO INESPERADO: {str(e)}", file=sys.stderr)
    finally:
        engine.dispose()
        print("\nConexão encerrada.")

if __name__ == "__main__":
    main()