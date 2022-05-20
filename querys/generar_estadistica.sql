-- Cantidad de registros totales por categoría

insert into estadistica_culturales_categoria(categoria, cantidad, fecha_carga)
select categoria, count(*) as cantidad, :fecha_carga as fecha_carga
from espacios_culturales
where fecha_carga = :fecha_carga
group by categoria;

-- Cantidad de registros totales por fuente
insert into estadistica_culturales_fuente(fuente, cantidad, fecha_carga)
select fuente, count(*) as cantidad, :fecha_carga as fecha_carga
from espacios_culturales
where fecha_carga = :fecha_carga
group by fuente;

-- Cantidad de registros por provincia y categoría
insert into estadistica_culturales_provincia(provincia, categoria, cantidad, fecha_carga)
select provincia,
       categoria,
       count(*) as cantidad,
       :fecha_carga    as fecha_carga
from espacios_culturales
where fecha_carga = :fecha_carga
group by categoria, provincia
;

---- Procesar la información de cines para poder crear una tabla que contenga:
-- Provincia
-- Cantidad de pantallas
-- Cantidad de butacas
-- Cantidad de espacios INCAA

insert into estadistica_cines
select provincia, sum(pantallas) as  pantallas , sum(butacas) as butacas , count(espacio_incaa) as espacio_incaa, :fecha_carga as fecha_carga
from espacios_culturales
where fecha_carga = :fecha_carga
and categoria = 'Salas de cine'
group by provincia
;
