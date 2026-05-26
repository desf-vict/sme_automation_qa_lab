-- SQL Report Queries
-- Purpose:
-- Practise reviewing SQL used by reporting automations before customer delivery.

-- ------------------------------------------------------------
-- 1. Valid query: sales report by customer.
-- ------------------------------------------------------------
SELECT
    customer_id,
    customer_name,
    SUM(order_total) AS total_sales
FROM orders
WHERE order_date >= '2026-01-01'
  AND order_date < '2026-02-01'
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC;

-- ------------------------------------------------------------
-- 2. Valid query: low-stock inventory report.
-- ------------------------------------------------------------
SELECT
    item_id,
    item_name,
    quantity,
    reorder_level
FROM inventory
WHERE quantity < reorder_level
ORDER BY quantity ASC;

-- ------------------------------------------------------------
-- 3. Defective query: misspelled SELECT and missing FROM.
-- ------------------------------------------------------------
SELEC customer_id, customer_name orders;

-- ------------------------------------------------------------
-- 4. Defective query: missing date filter.
-- Risk:
-- This may produce a full historical report instead of the requested period.
-- ------------------------------------------------------------
SELECT
    customer_id,
    customer_name,
    order_total
FROM orders;

-- ------------------------------------------------------------
-- 5. Risky query: destructive action.
-- Risk:
-- This should not be allowed in a reporting automation without explicit approval.
-- ------------------------------------------------------------
DELETE FROM orders;

-- ------------------------------------------------------------
-- 6. Defective query: unquoted string value.
-- ------------------------------------------------------------
SELECT
    *
FROM customers
WHERE status = active;

-- ------------------------------------------------------------
-- 7. Valid query: customer records updated this month.
-- ------------------------------------------------------------
SELECT
    customer_id,
    customer_name,
    updated_at
FROM customers
WHERE updated_at >= '2026-05-01'
  AND updated_at < '2026-06-01'
ORDER BY updated_at DESC;
