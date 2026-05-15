drop table if exists tb_locacoes cascade;
drop table if exists tb_veiculos cascade;

create table tb_veiculos (
    placa varchar(10) primary key,
    categoria varchar(50) not null,
    taxa_diaria numeric(10,2) not null,
    estado_atual varchar(50) not null,
    tipo varchar(50) not null
);

create table tb_locacoes (
    id serial primary key,
    veiculo_id varchar(10) references tb_veiculos(placa),
    data_inicio date not null,
    data_fim date not null,
    status varchar(20) default 'reservado',
    valor_total numeric(10,2) default 0
);

insert into tb_veiculos
(
    placa,
    categoria,
    taxa_diaria,
    estado_atual,
    tipo
)
values
(
    'AAA1111',
    'economico',
    100,
    'disponivel',
    'carro'
);

insert into tb_locacoes
(
    veiculo_id,
    data_inicio,
    data_fim,
    status,
    valor_total
)
values
(
    'AAA1111',
    current_date,
    current_date + 3,
    'reservado',
    300
);

select * from tb_veiculos;
select * from tb_locacoes;
select current_database();