# -- 코드를 입력하세요
# SELECT warehouse_id, warehouse_name, address, ifnull(freezer_yn, 'N') as 'FREEZER_YN'
# from food_warehouse
# where address like '%경기도%'
# order by warehouse_id;





select warehouse_id, warehouse_name, address, 
    case
        when freezer_yn is null then 'N'
        else freezer_yn
        end as freezer_yn
from food_warehouse
where warehouse_name like '%경기%'
order by warehouse_id;

















