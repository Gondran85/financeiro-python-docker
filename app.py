
# Importa o módulo que permite acessar variáveis de ambiente
import os
# Importa a função de cálculo de saldo financeiro
from financeiro import calcular_saldo

# Lê os valores enviados pelo ambiente
# Se não forem informados, utiliza os valores padrão
receita = float(os.getenv("RECEITA", "5000"))
despesas = float(os.getenv("DESPESAS", "3200"))

# Calcula o saldo restante
saldo = calcular_saldo(receita, despesas)


if saldo < 0:
    print("=== ALERTA FINANCEIRO ===")
    print()
    print(f"Receita: R$ {receita:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print()
    print("Atenção: saldo negativo!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Por favor, reveja suas despesas.")
elif saldo == 0:
    print("=== ALERTA FINANCEIRO ===")
    print()
    print(f"Receita: R$ {receita:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print()
    print("Atenção: saldo zerado!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Tente economizar nas próximas despesas.")
else:
    print("=== ALERTA FINANCEIRO ===")
    print()
    print(f"Receita: R$ {receita:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print()
    print("Saldo positivo!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Continue mantendo suas finanças equilibradas.")



