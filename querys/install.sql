-- create database "alkemy";
-- grant all privileges on database alkemy to admin;
-- cod_localidad
-- id_provincia
-- id_departamento
-- categoría
-- provincia
-- localidad
-- nombre
-- domicilio
-- código postal
-- número de teléfono
-- mail
-- web
-- fecha_carga

create table if not exists espacios_culturales (
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    categoria varchar(50),
    provincia varchar(100),
    localidad varchar(50),
    nombre varchar(255),
    domicilio varchar(255),
    cod_postal varchar(50),
    telefono varchar(50),
    mail varchar(255),
    web varchar(255),
    fuente varchar(255),
    pantallas integer,
    butacas integer,
    espacio_incaa varchar(10),
    fecha_carga date
);
-- Cantidad de registros totales por categoría
-- Cantidad de registros totales por fuente
-- Cantidad de registros por provincia y categoría
-- fecha_carga


create table if not exists estadistica_culturales_categoria(
    categoria varchar(50),
    cantidad integer,
    fecha_carga date
); 
create table if not exists estadistica_culturales_fuente(
    fuente varchar(255),
    cantidad integer,
    fecha_carga date
); 

create table if not exists estadistica_culturales_provincia(
    categoria varchar(50),
    provincia varchar(100),
    cantidad integer,
    fecha_carga date
); 


-- Procesar la información de cines para poder crear una tabla que contenga:
-- Provincia
-- Cantidad de pantallas
-- Cantidad de butacas
-- Cantidad de espacios INCAA

create table if not exists estadistica_cines (
    provincia varchar(50),
    cantidad_pantallas integer,
    cantidad_butacas integer,
    cantidad_incaa integer,
    fecha_carga date
);


create table if not exists espacios_culturales (
    id serial primary key,
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    categoria varchar(50),
    provincia varchar(50),
    localidad varchar(50),
    nombre varchar(255),
    domicilio varchar(255),
    cod_postal integer,
    telefono varchar(50),
    mail varchar(50),
    web varchar(255),
    fecha_carga date
);

-- Cantidad de registros totales por categoría
-- Cantidad de registros totales por fuente
-- Cantidad de registros por provincia y categoría
-- fecha_carga

create table if not exists estadistica_espacios_culturales(
    id serial primary key,
    fuente varchar(20),
    categoria varchar(50),
    provincia varchar(50),
    total_fuente integer,
    total_categoria integer,
    q_registros integer,
    fecha_carga date
);

-- Procesar la información de cines para poder crear una tabla que contenga:
-- Provincia
-- Cantidad de pantallas
-- Cantidad de butacas
-- Cantidad de espacios INCAA
create table if not exists estadistica_cines (
    id serial primary key,
    provincia varchar(50),
    cantidad_pantallas integer,
    cantidad_butacas integer,
    cantidad_incaa integer,
    fecha_carga date
);