select * from sales;
use ecommerce;
-- total sale in table 
select
   sum(sales) as total_sale
from sales;

-- total profit from sales
select 
    sum(profit) as total_profit
from sales;

-- total sale according region wise 
select 
   region,
   sum(sales) as total_sale
from sales
group by region
order by total_sale desc;

-- profit according region wise 
select
    region,
    sum(profit) as total_profit
from sales
group by region
order by total_profit desc;

-- top 5 city which do higest sale 
select
   city,
   sum(sales) as total_sale
from sales
group by city
order by total_sale desc
limit 5;

-- primium customer 
select count(distinct customer_name)as unique_customer
from sales;
select * from sales;
-- top 5 product according sale
select
   product_name,
   sum(sales)as total_sale,
   sum(profit) as total_profit
from sales
group by product_name
order by total_sale,total_profit desc
limit 5;

-- profit margin
SELECT 
    category,
    SUM(profit)/SUM(sales) * 100 AS profit_margin
FROM sales
GROUP BY category
ORDER BY profit_margin DESC;
-- montly trend
SELECT 
    MONTH(order_date) AS month,
    SUM(sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;

-- year trend
select
    year(order_date) as year,
    sum(sales) as total_sale
from sales
group by year
order by year;