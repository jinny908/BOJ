-- 코드를 입력하세요
# 2022년 11월 1일 부터 2022년 11월 30일까지 대여 가능하고 30일간의 50만원 <= 대여금액 <200만원 인 자동차id, 자동차 종류, 대여금액
# with available as (
# select a.car_id, a.car_type, a.daily_fee, c.discount_rate, c.duration_type
# from car_rental_company_car a join car_rental_company_discount_plan c on a.car_type = c.car_type and c.duration_type = '30일 이상'
# where a.car_type in ('세단','SUV') and a.car_id not in
#     (select car_id from car_rental_company_rental_history
#     where end_date >= '2022-11-01' and start_date <= '2022-11-30') 
# )

# select car_id, car_type, round(daily_fee *30* (100 - discount_rate) / 100,0) as fee from available
# where round(daily_fee * 30* (100 - discount_rate) / 100,0) between 500000 and 1999999
# order by fee desc, car_type, car_id desc
# ;

    
select a.car_id, a.car_type, round(a.daily_fee * 30 * (100 - c.discount_rate) / 100, 0) as fee 
from car_rental_company_car a join car_rental_company_discount_plan c on a.car_type = c.car_type and c.duration_type = "30일 이상"
where a.car_type in ('세단','SUV') and a.car_id not in (
select b.car_id from car_rental_company_rental_history b
    where b.start_date <= '2022-11-30' and b.end_date >= '2022-11-01'
) and round(a.daily_fee * 30 * (100 - c.discount_rate) / 100, 0) between 500000 and 1999999
order by fee desc, a.car_type, a.car_id desc;
