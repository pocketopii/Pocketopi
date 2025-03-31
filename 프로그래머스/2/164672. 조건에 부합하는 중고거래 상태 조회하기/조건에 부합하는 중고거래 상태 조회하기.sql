SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, CASE STATUS   WHEN 'DONE' THEN '거래완료'
                                                        WHEN 'SALE' THEN '판매중'
                                                        ELSE '예약중' END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY 1 DESC