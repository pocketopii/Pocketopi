SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK INNER JOIN BOOK_SALES
ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE MONTH(SALES_DATE) = 1 
GROUP BY 1
ORDER BY 1