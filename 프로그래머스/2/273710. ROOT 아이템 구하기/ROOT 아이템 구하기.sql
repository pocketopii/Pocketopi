SELECT ITEM_ID, ITEM_NAME
FROM ITEM_INFO I NATURAL JOIN ITEM_TREE T
WHERE PARENT_ITEM_ID IS NULL
ORDER BY 1