class aparelho:
    def __init__(self, modelo, marca, tipo, quantidade, preco_aparelho, aparelhosId=None):
        self.aparelhosId = aparelhosId
        self.modelo = modelo
        self.marca = marca
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco_aparelho = preco_aparelho
    def __repr__(self):
        return f"\nAparelho(aparelhosId={self.aparelhosId},\n modelo='{self.modelo}', \nmarca='{self.marca}',\n tipo='{self.tipo}', \nquantidade={self.quantidade}, \npreco_aparelho={self.preco_aparelho})"

class Comprador:
    def __init__(self, nome_comprador, data_compra, id_compradores, id=None):
        self.id = id
        self.nome_comprador = nome_comprador
        self.data_compra = data_compra
        self.id_compradores = id_compradores
        def __repr__(self):
         return f"Comprador(id={self.id}, nome_comprador='{self.nome_comprador}', data_compra='{self.data_compra}', id_aparelho={self.id_compradores})"

    