SELECT PRODUCT_ID, NEW_PRICE AS PRICE
FROM PRODUCTS
WHERE (PRODUCT_ID, CHANGE_DATE) IN (SELECT PRODUCT_ID, MAX(CHANGE_DATE) 
                                    FROM PRODUCTS
                                    WHERE CHANGE_DATE <= '2019-08-16'
                                    GROUP BY PRODUCT_ID)

UNION

SELECT PRODUCT_ID, 10 AS PRICE
FROM PRODUCTS
WHERE (PRODUCT_ID, CHANGE_DATE) IN (SELECT PRODUCT_ID, MIN(CHANGE_DATE) 
                                    FROM PRODUCTS
                                    GROUP BY PRODUCT_ID
                                    HAVING MIN(CHANGE_DATE) > '2019-08-16')