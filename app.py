
# Importa o módulo que permite acessar variáveis de ambiente
import os

# Lê os valores enviados pelo ambiente
# Se não forem informados, utiliza os valores padrão
receita = float(os.getenv("RECEITA", "5000"))
despesas = float(os.getenv("DESPESAS", "3200"))

# Calcula o saldo restante
saldo = receita - despesas

# Apresenta os resultados financeiros
print("=== SISTEMA FINANCEIRO ===")
print(f"Receita: R$ {receita:.2f}")
print(f"Despesas: R$ {despesas:.2f}")
print(f"Saldo: R$ {saldo:.2f}")

