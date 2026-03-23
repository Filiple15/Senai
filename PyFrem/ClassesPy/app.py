

from cliente.cliente import Cliente
from produto.produto import Produto

# Clientes
c1 = Cliente("FLsantos", "joaozinho96@ggmail.cain", 16, "15/11", "M")
c2 = Cliente("Maria", "maria@email.com", 22, "02/02/2003", "F")
c3 = Cliente("Ana", "ana@email.com", 19, "03/03/2006", "F")

# Produtos
p1 = Produto("Notebook", 3000, 2)
p2 = Produto("Mouse", 100, 5)
p3 = Produto("Teclado", 200, 3)

# Mostrar clientes
for cliente in [c1, c2, c3]:
    cliente.exibir_informacoes()
    print("Nome:", cliente.nome)
    print("Idade:", cliente.idade)
    print("-----")

# Mostrar produtos
for produto in [p1, p2, p3]:
    print("Produto:", produto.nome)
    print("Preço:", produto.preco)
    print("Valor total:", produto.valor_total())
    print("-----")