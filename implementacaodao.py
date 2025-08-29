import psycopg2
from interfaceDao import AparelhoDAOInterface, CompradorDAOInterface
from modelo import aparelho, Comprador
from datetime import date

DB_CONFIG = 'postgresql://novo_usuario:nada123@localhost:5432/novo_banco_de_dados'

class AparelhoDAOPostgreSQL(AparelhoDAOInterface):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(DB_CONFIG)
            self.cursor = self.conn.cursor()
            return self
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def _execute_query(self, query, params=None, commit=False):
        try:
            self.cursor.execute(query, params)
            if commit:
                self.conn.commit()
            return self.cursor
        except psycopg2.Error as e:
            print(f"Erro na execucao da consulta: {e}")
            self.conn.rollback()
            return None

    def create(self, aparelho: aparelho):
        query = "INSERT INTO aparelhos (modelo, marca, tipo, quantidade, preco_aparelho) VALUES (%s, %s, %s, %s, %s) RETURNING aparelhosid"
        params = (aparelho.modelo, aparelho.marca, aparelho.tipo, aparelho.quantidade, aparelho.preco_aparelho)
        cursor = self._execute_query(query, params, commit=True)
        if cursor:
            aparelho.aparelhosId = cursor.fetchone()[0]
            return aparelho
        return None

    def read(self, aparelho_id: int):
        query = "SELECT aparelhosid, modelo, marca, tipo, quantidade, preco_aparelho FROM aparelhos WHERE aparelhosid = %s"
        cursor = self._execute_query(query, (aparelho_id,))
        if cursor:
            row = cursor.fetchone()
            if row:
                return aparelho(aparelhosId=row[0], modelo=row[1], marca=row[2], tipo=row[3], quantidade=row[4], preco_aparelho=row[5])
        return None

    def update(self, aparelho: aparelho):
        query = "UPDATE aparelhos SET modelo=%s, marca=%s, tipo=%s, quantidade=%s, preco_aparelho=%s WHERE aparelhosid = %s"
        params = (aparelho.modelo, aparelho.marca, aparelho.tipo, aparelho.quantidade, aparelho.preco_aparelho, aparelho.aparelhosId)
        cursor = self._execute_query(query, params, commit=True)
        return cursor and cursor.rowcount > 0

    def delete(self, aparelho_id: int):
        query = "DELETE FROM aparelhos WHERE aparelhosid = %s"
        cursor = self._execute_query(query, (aparelho_id,), commit=True)
        return cursor and cursor.rowcount > 0

    def list_all(self):
        query = "SELECT aparelhosid, modelo, marca, tipo, quantidade, preco_aparelho FROM aparelhos"
        cursor = self._execute_query(query)
        if cursor:
            return [aparelho(aparelhosId=row[0], modelo=row[1], marca=row[2], tipo=row[3], quantidade=row[4], preco_aparelho=row[5]) for row in cursor.fetchall()]
        return []

    def sum_quantity(self):
        query = "SELECT SUM(quantidade) FROM aparelhos"
        cursor = self._execute_query(query)
        if cursor:
            result = cursor.fetchone()[0]
            return result if result is not None else 0
        return 0

    def select_min_max_price(self):
        query = "SELECT MAX(preco_aparelho), MIN(preco_aparelho) FROM aparelhos"
        cursor = self._execute_query(query)
        if cursor:
            return cursor.fetchone()
        return (None, None)

class CompradorDAOPostgreSQL(CompradorDAOInterface):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def _execute_query(self, query, params=None, commit=False):
        try:
            self.cursor.execute(query, params)
            if commit:
                self.conn.commit()
            return self.cursor
        except psycopg2.Error as e:
            print(f"Erro na execucao da consulta de comprador: {e}")
            self.conn.rollback()
            return None

    def create(self, comprador: Comprador):
        query = "INSERT INTO compradores (nome_comprador, data_compra, id_compradores) VALUES (%s, %s, %s) RETURNING nome_comprador"
        params = (comprador.nome_comprador, comprador.data_compra, comprador.id_compradores)
        cursor = self._execute_query(query, params, commit=True)
        if cursor:
            comprador.id = cursor.fetchone()[0]
            return comprador
        return None

    def get_by_aparelho_id(self, aparelho_id: int):
        query = "SELECT nome_comprador, data_compra, id_compradores FROM compradores WHERE id_compradores = %s"
        cursor = self._execute_query(query, (aparelho_id,))
        if cursor:
            row = cursor.fetchone()
            if row:
                return Comprador(id=row[0], nome_comprador=row[0], data_compra=row[1], id_compradores=row[2])
        return None
    
    def list_all(self):
        query = "SELECT nome_comprador, data_compra, id_compradores FROM compradores"
        cursor = self._execute_query(query)
        if cursor:
            compradores = []
            for row in cursor.fetchall():
                compradores.append(Comprador(id=row[0], nome_comprador=row[0], data_compra=row[1], id_compradores=row[2]))
            return compradores
        return []