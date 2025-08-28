CREATE DATABASE novo_banco_de_dados;
novo_banco_de_dados=> CREATE TABLE aparelhos (
    aparelhosId serial PRIMARY KEY,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    tipo text not null,
    quantidade int not null,
    preco_aparelho int not null
);

create table compradores(
    nome_comprador varchar(50) unique not null,
    data_compra date not null,
    id_compradores bigint references aparelhos(aparelhosId)
);
