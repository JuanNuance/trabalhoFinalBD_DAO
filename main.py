from implementacaodao import AparelhoDAOPostgreSQL
from modelo import aparelho

with AparelhoDAOPostgreSQL() as aparelho_dao:
    if aparelho_dao:
        aparelho1 = aparelho(modelo="a51", marca="samsung", tipo="celular", quantidade=5, preco_aparelho=700)
        aparelho2 = aparelho(modelo='vision r15', marca='positivo', tipo='notebook', quantidade=2, preco_aparelho=800)

        aparelho_salvo1 = aparelho_dao.create(aparelho1)
        aparelho_salvo2 = aparelho_dao.create(aparelho2)
        print("Aparelhos salvos:", aparelho_dao.list_all())

        aparelho_encontrado = aparelho_dao.read(aparelho_salvo1.aparelhosId)
        if aparelho_encontrado:
            print(f"\nAparelho encontrado: {aparelho_encontrado}")

        aparelho_encontrado.preco_aparelho = 2000
        aparelho_dao.update(aparelho_encontrado)
        print(f"\nAparelho atualizado: {aparelho_dao.read(aparelho_encontrado.aparelhosId)}")

        aparelho_dao.delete(aparelho_salvo2.aparelhosId)
        print("\nApós deletar um aparelho, a lista agora é:", aparelho_dao.list_all())
    else:
        print("Não foi possível conectar ao banco de dados.")

       
    print("\nLista de todos os aparelhos:", aparelho_dao.list_all())
       
    print("\nSoma da quantidade de aparelhos:", aparelho_dao.sum_quantity())
      
    min_price, max_price = aparelho_dao.select_min_max_price()
    print(f"\nAparelho com menor preço: {min_price}")
    print(f"Aparelho com maior preço: {max_price}")