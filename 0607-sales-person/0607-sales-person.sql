SELECT NAME
FROM SALESPERSON
WHERE SALES_ID NOT IN (SELECT SALES_ID
                   FROM COMPANY NATURAL JOIN ORDERS
                   WHERE NAME = 'RED')