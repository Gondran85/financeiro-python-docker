
# Importa a biblioteca de testes do Python
import unittest

# Importa a função que queremos testar
from financeiro import calcular_saldo


# Classe que agrupa os testes financeiros
class TesteFinanceiro(unittest.TestCase):

    # Verifica se o cálculo de saldo positivo está correto
    def test_saldo_positivo(self):

        # Executa a função com valores conhecidos
        resultado = calcular_saldo(5000, 3200)

        # Compara o resultado real com o esperado
        self.assertEqual(resultado, 1800)
            # Verifica se o cálculo de saldo negativo está correto
    def test_saldo_negativo(self):

        # Executa a função com valores conhecidos
        resultado = calcular_saldo(3000, 3200)

        # Compara o resultado real com o esperado
        self.assertEqual(resultado, -200)

    # Verifica se o cálculo de saldo zerado está correto
    def test_saldo_zerado(self):

        # Executa a função com valores conhecidos
        resultado = calcular_saldo(3200, 3200)

        # Compara o resultado real com o esperado
        self.assertEqual(resultado, 0)