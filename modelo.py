class aparelho:
    def __init__(self, modelo, marca, tipo, quantidade, preco_aparelho, aparelhosId=None):
        self.aparelhosId = aparelhosId
        self.modelo = modelo
        self.marca = marca
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco_aparelho = preco_aparelho

    def __repr__(self):
        return f"Aparelho(aparelhosId={self.aparelhosId}, modelo='{self.modelo}', marca='{self.marca}', tipo='{self.tipo}', quantidade={self.quantidade}, preco_aparelho={self.preco_aparelho})"