select b.id, b.email, b.first_name, b.last_name from skillcodes a join developers b on (b.skill_code & a.code) != 0
where a.category = "Front End"
GROUP BY b.id, b.email, b.first_name, b.last_name
order by b.id;
