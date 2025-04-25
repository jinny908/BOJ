# -- 코드를 입력하세요
SELECT a.flavor
from first_half a join july b on a.flavor = b.flavor
group by a.flavor
order by a.total_order + sum(b.total_order) desc
limit 3;

# select a.flavor from first_half a join july b on a.shipment_id = b.shipment_id
# group by a.flavor
# order by (a.total_order + b.total_order) desc
# limit 3

# ;

















