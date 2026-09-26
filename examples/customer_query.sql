SELECT customer_id, customer_name
FROM customers
WHERE customer_id = 123
  AND status = 'ACTIVE'
  AND created_date >= DATE '2026-01-01';
