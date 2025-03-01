select employees.name, employees.salary, departments.department_name 
from employees 
inner join  departments ON employees.department_id = departments.id;