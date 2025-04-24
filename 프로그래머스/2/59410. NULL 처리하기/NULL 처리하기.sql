# -- 코드를 입력하세요
# SELECT animal_type, ifnull(name, 'No name') as name, sex_upon_intake from animal_ins
# order by animal_id







select animal_type, 
    case
        when name is null then 'No name'
        else name
        end
        , sex_upon_intake
        from animal_ins
order by animal_id

;




















