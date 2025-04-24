-- 코드를 입력하세요
# SELECT month(start_date) as month , car_id, count(*) as records from car_rental_company_rental_history
# where month(start_date) >= 8 and month(start_date) <= 10 
# and car_id in (select car_id from car_rental_company_rental_history where month(start_date) >= 8 and month(start_date) <= 10 group by car_id having count(*) >= 5)
# group by month, car_id
# having records > 0
# order by month, car_id desc;

select month(start_date) as month, car_id, count(*) as records from car_rental_company_rental_history
where month(start_date) between 8 and 10
and car_id in 
(
    select car_id from car_rental_company_rental_history 
    where month(start_date) between 8 and 10 
    group by car_id
    having count(*) >= 5
)
group by month(start_date), car_id
order by month, car_id desc;