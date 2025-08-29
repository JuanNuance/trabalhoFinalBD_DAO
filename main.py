from implementacaodao import AparelhoDAOPostgreSQL, CompradorDAOPostgreSQL
from modelo import aparelho, Comprador
from datetime import date

def main():
    with AparelhoDAOPostgreSQL() as aparelho_dao:
        if not aparelho_dao:
            print("Nao foi possível conectar ao banco de dados.")
            return

        print("\n--- Criando novos aparelhos ---")
        aparelho1 = aparelho(modelo="a51", marca="samsung", tipo="celular", quantidade=5, preco_aparelho=700)
        aparelho2 = aparelho(modelo='vision r15', marca='positivo', tipo='notebook', quantidade=2, preco_aparelho=800)

        aparelho_salvo1 = aparelho_dao.create(aparelho1)
        aparelho_salvo2 = aparelho_dao.create(aparelho2)

        if aparelho_salvo1:
            print(f"Aparelho 1 salvo com sucesso: {aparelho_salvo1}")
        else:
            print("Falha ao salvar o aparelho 1.")

        if aparelho_salvo2:
            print(f"Aparelho 2 salvo com sucesso: {aparelho_salvo2}")
        else:
            print("Falha ao salvar o aparelho 2.")
        
        print("\nLista atual de aparelhos:", aparelho_dao.list_all())

        if aparelho_salvo1:
            print(f"\n--- Atualizando o aparelho ID: {aparelho_salvo1.aparelhosId} ---")
            aparelho_salvo1.preco_aparelho = 2000
            if aparelho_dao.update(aparelho_salvo1):
                print(f"Aparelho atualizado: {aparelho_dao.read(aparelho_salvo1.aparelhosId)}")
            else:
                print("\nFalha ao atualizar o aparelho.")

        if aparelho_salvo2:
            print(f"\n--- Deletando o aparelho ID: {aparelho_salvo2.aparelhosId} ---")
            if aparelho_dao.delete(aparelho_salvo2.aparelhosId):
                print("Aparelho deletado com sucesso.")
            else:
                print("Falha ao deletar o aparelho.")
            print("\nLista apos deletacao:", aparelho_dao.list_all())
        
        if aparelho_salvo1 and aparelho_dao.read(aparelho_salvo1.aparelhosId):
            print(f"\n--- Associando Comprador ao aparelho ID: {aparelho_salvo1.aparelhosId} ---")
            comprador_dao = CompradorDAOPostgreSQL(aparelho_dao.conn)
            
            novo_comprador = Comprador(
                nome_comprador="Joao Silva",
                data_compra=date.today(),
                id_compradores=aparelho_salvo1.aparelhosId
            )
            comprador_salvo = comprador_dao.create(novo_comprador)
            if comprador_salvo:
                print(f"Comprador salvo e associado: {comprador_salvo}")
            else:
                print("\nFalha ao salvar o comprador.")

        print("\n--- Consultas Finais ---")
        print("Lista de todos os compradores:", comprador_dao.list_all())
        print("\nLista de todos os aparelhos:", aparelho_dao.list_all())
        print("\nSoma da quantidade de aparelhos:", aparelho_dao.sum_quantity())
        
        precos = aparelho_dao.select_min_max_price()
        if precos and precos[0] is not None:
             max_price, min_price = precos
             print(f"Aparelho com maior preço: {max_price}")
             print(f"Aparelho com menor preço: {min_price}")
        else:
             print("\nNao ha aparelhos para calcular preço máximo e mínimo.")
if __name__ == "__main__":
    main()