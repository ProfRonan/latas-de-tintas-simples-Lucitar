print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
# 1 litro = 3 m²
# 1 lata = 18 litros
# 1 lata = 54 m²

qtd_de_latas = metros_quadrados // 54
if(metros_quadrados / 54 > qtd_de_latas):
  qtd_de_latas = qtd_de_latas + 1
valor_total = qtd_de_latas * 80

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.


print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
