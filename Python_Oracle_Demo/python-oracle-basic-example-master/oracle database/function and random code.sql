--Christian Ruales
-- don't forget execute a commit after of execute any command
----------------alter add column
alter table libros_pedido
add (usuario_id number(4) NOT NULL);

-------------------------alter create relation
alter table libros_pedido
add constraint FK_USUARIO_ID FOREIGN KEY(usuario_id)
REFERENCES usuario(id_usuario);

---------------- creating sequence for id_libros_pedido
create sequence seq_id_libros_pedido
start with 1
increment by 1
minvalue 1;

-- alter add column x2
alter table libros_pedido
add( cantidad number(4) NOT NULL);
commit

--renombrar columna de una tabla
alter table libros_pedido
rename column pedido_id to id_pedido;

--anadir primary key ocn alter
alter table libros_pedido
add constraint PK_ID_PEDIDO PRIMARY KEY(id_pedido)

commit




--funcion verificar stock de libros
create or replace function func_verify_stock(isb in varchar, rented_books in number)
return number is
    v_quantity number;
    v_verify number;
    v_new_quantity number;
begin
    select cantidad into v_quantity from libros where ISB=isbn;
    
    
    
    if v_quantity=0 then
        v_verify:=0;
    else
        if rented_books<=v_quantity then
            v_new_quantity:=v_quantity-rented_books;
            v_verify:=v_new_quantity;
            
               
        else
            v_verify:=0;
        end if;
    end if;
return v_verify;
end func_verify_stock;
/
commit


---------Select RANDOMS
select nombre, libros_pedido.cantidad, usuario from libros, usuario, libros_pedido where libros_pedido.isbn=libros.isbn and libros_pedido.usuario_id=usuario.id_usuario and usuario_id=52
select * from usuario
insert into libros_pedido(id_pedido,ISBN, usuario_id, cantidad) values(seq_id_libros_pedido.nextval,'1234567890123',52,3)
select * from libros_pedido;

select * from usuario where usuario='chr123'

select * from libros_pedido where usuario_id=52
SELECT * FROM libros

update libros set cantidad=7 where ISBN='1234567890123'

select func_verify_stock('1234567890123',1) from dual;
select * from pedidos
drop table pedidos cascade constraints
commit;
desc usuario;
DESC libros_pedido
commit