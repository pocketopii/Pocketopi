SELECT PRODUCT_ID, YEAR AS FIRST_YEAR, QUANTITY, PRICE
FROM SALES NATURAL JOIN PRODUCT
WHERE (PRODUCT_ID, YEAR) IN (SELECT PRODUCT_ID, MIN(YEAR)
                            FROM SALES
                            GROUP BY 1)