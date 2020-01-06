import mysql

mysqlResult = mysql.selectBD('select * from v_funcionarios')
for dado in mysqlResult:
    print(dado['cpf'])