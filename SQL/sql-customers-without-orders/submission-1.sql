-- Write your query below
select c.name from customers c
where not exists (
    select 1 from orders o
    where o.customer_id = c.id
)