select * from (
    select *, row_number() over (order by salary desc) as row_num 
    from employees
) as ranked_employees
where row_num <= 3;