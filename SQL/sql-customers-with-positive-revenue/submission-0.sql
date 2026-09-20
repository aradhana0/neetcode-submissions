-- Write your query below
-- positive revenue in the year 2020
-- Return only the customer_id
-- the result can be returned in any order

select customer_id from customers where revenue > 0 and year = 2020