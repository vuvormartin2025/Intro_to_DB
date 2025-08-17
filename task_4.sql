-- task_4.sql
-- Script to print the full description of the table books
-- from the database alx_book_store

SELECT COLUMN_NAME,
       COLUMN_TYPE,
       IS_NULLABLE,
       COLUMN_KEY,
       COLUMN_DEFAULT,
       EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'books';