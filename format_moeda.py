# Define o valor como 1768
valor = 1768

# Formata o valor como uma string no formato monetário brasileiro
# com duas casas decimais e separador de milhares
valor_real = "R${:,.2f}".format(valor)

# Substitui as vírgulas por uma letra 'X'
# para evitar a substituição incorreta na próxima etapa
valor_real = valor_real.replace(",", "X")

# Substitui os pontos por vírgulas
valor_real = valor_real.replace(".", ",")

# Substitui as letras 'X' por pontos novamente,
# restaurando o formato original
valor_real = valor_real.replace("X", ".")

# Imprime o valor formatado
print(valor_real)
