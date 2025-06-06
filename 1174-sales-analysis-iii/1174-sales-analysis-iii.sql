SELECT PRODUCT_ID, PRODUCT_NAME
FROM PRODUCT
WHERE PRODUCT_ID IN (SELECT PRODUCT_ID
                     FROM SALES
                     GROUP BY PRODUCT_ID
                     HAVING MIN(SALE_DATE) >= "2019-01-01" AND MAX(SALE_DATE) <= "2019-03-31")