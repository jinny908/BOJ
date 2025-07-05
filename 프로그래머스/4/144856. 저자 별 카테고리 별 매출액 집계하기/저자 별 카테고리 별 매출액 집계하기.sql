-- 코드를 입력하세요
# SELECT a.author_id, b.author_name, a.category, sum(a.price * c.sales) as total_sales
# from book a join author b on a.author_id = b.author_id join book_sales c on a.book_id = c.book_id
# where date_format(c.sales_date,'%Y-%m') like ('2022-01%')
# group by a.author_id, a.category
# order by a.author_id, a.category desc;


select a.author_id, b.author_name, a.category, sum(a.price * c.sales) as total_sales
from book a join author b on a.author_id = b.author_id join book_sales c on a.book_id = c.book_id
where date_format(c.sales_date, '%y-%m') = '22-01'
group by a.author_id, a.category
order by a.author_id, a.category desc;