
-- Total sales by city
SELECT city, SUM(total_amount) AS total_sales
FROM sales_data
GROUP BY city;

-- Top selling products
SELECT product_id, SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY product_id
ORDER BY total_quantity DESC;

-- Daily sales trend
SELECT order_date, SUM(total_amount) AS daily_sales
FROM sales_data
GROUP BY order_date
ORDER BY order_date;
