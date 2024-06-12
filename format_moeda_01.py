import locale  # Importa o módulo locale para formatação local

# Define a localidade para formatação monetária como 'en-US' (inglês dos Estados Unidos)
locale.setlocale(locale.LC_MONETARY, 'en-US')
# Formata o valor 15000.0 como moeda usando a localidade definida e agrupa os milhares
valor_em_dolar_formatado = locale.currency(15000.0, grouping=True)
# Imprime o valor formatado como moeda em dólar
print(valor_em_dolar_formatado)
# Saída esperada: $15,000.00

# Define a localidade para formatação monetária como 'pt-PT' (português de Portugal)
locale.setlocale(locale.LC_MONETARY, 'pt-PT')
# Formata o valor 15000.0 como moeda usando a nova localidade definida e agrupa os milhares
valor_em_dolar_formatado = locale.currency(15000.0, grouping=True)
# Imprime o valor formatado como moeda em euro
print(valor_em_dolar_formatado)
# Saída esperada: 15.000,00 €

