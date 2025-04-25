# -- 코드를 입력하세요
# SELECT b.product_id, a.product_name, sum(price*amount) as total_sales
# from food_product a join food_order b on a.product_id = b.product_id
# where date_format(produce_date, '%Y-%m') = '2022-05' 
# group by product_name
# order by total_sales desc, product_id;

select a.product_id, a.product_name, 
    case
        when date_format(b.produce_date, '%Y-%m') = '2022-05' then sum(b.amount * a.price)
        else 0
    end as total_sales
from food_product a join food_order b on a.product_id = b.product_id
where date_format(b.produce_date, '%Y-%m') = '2022-05'
group by a.product_name
order by total_sales desc, a.product_id
;





















