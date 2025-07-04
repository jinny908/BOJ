# -- 코드를 입력하세요
# SELECT order_id, product_id, date_format(out_date,'%Y-%m-%d') as out_date, 
# case 
#     when datediff(out_date,'2022-05-01') > 0 then '출고대기'
#     when datediff(out_date,'2022-05-01') <= 0 then '출고완료'
# else
#     '출고미정'
# end as '출고여부'
# from food_order
# order by order_id;

select order_id, product_id, date_format(out_date, '%Y-%m-%d') as out_date,
    case
        when datediff(out_date, '2022-05-01') > 0 then '출고대기'
        when datediff(out_date, '2022-05-01') <= 0 then '출고완료'
        else '출고미정'
    end as '출고여부'
from food_order
order by order_id;
        