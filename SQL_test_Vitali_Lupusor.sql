/*
Date: 2020-11-01
Author: Vitali Lupusor

Description: TimeOut practical SQL test.
    The below query is written with BigQuery SQL syntax in mind, 
    however, if needed, it can be translated to any other SQL dialect.
*/

WITH
  sales AS (
  SELECT
    product,
    PARSE_DATE('%d/%m/%Y',                              -- Parsing the date string to appropriate format
      sales_date) AS sales_date,
    quantity
  FROM
    `project.table.Sales`),
  prices_proxy AS (
  SELECT
    product,
    PARSE_DATE('%d/%m/%Y',                              -- Parsing the date string to appropriate format
      price_effective_date) AS price_effective_date,
    price
  FROM
    `project.table.Prices`),
  prices AS (                                           -- Joining the table to itself to create the end data of the price change
  SELECT
    price_0.product,
    price_0.price_effective_date AS start_date,
    CASE                                                -- Filling in the blank to account for the latest change
      WHEN price_1.price_effective_date IS NULL THEN CURRENT_DATE()
    ELSE
    DATE_SUB(price_1.price_effective_date, INTERVAL 1 DAY)
  END
    AS end_date,
    price_0.price
  FROM
    prices_proxy AS price_0
  LEFT JOIN
    prices_proxy AS price_1
  ON
    price_0.product = price_1.product
    AND price_0.price_effective_date < price_1.price_effective_date
  LEFT JOIN
    prices_proxy AS price_2
  ON
    price_0.product = price_2.product
    AND price_0.price_effective_date < price_2.price_effective_date
    AND price_1.price_effective_date > price_2.price_effective_date
  WHERE
    price_2.price_effective_date IS NULL),
  joined_table AS (
  SELECT
    CAST(price AS INT64) AS price,                  -- Converting to Integer, in case the column is of String type
    CAST(quantity AS INT64) AS quantity             -- Converting to Integer, in case the column is of String type
  FROM
    sales
  JOIN
    prices
  ON
    sales.product = prices.product
    AND prices.start_date <= sales.sales_date
    AND sales.sales_date < prices.end_date)
SELECT
  SUM(price * quantity) AS total_revenue            -- Print out the total revenue. If more insights are needed, 
FROM                                                -- it can be grouped by sales date and product.
  joined_table                                      -- We can also analyse the sales based on price fluctuation.
