import mysql
import regex


# Fabio Casaroli
# Biblioteca de Login

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == '1':
        nome = input('digite seu login: ')
        senha = input('digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    return ['nivel 1']
                    return True
                elif linha['nivel'] == 2:
                    return ['nivel 2']
                    return True
            elif nome == linha['nome'] and senha != linha['senha']:
                return ('Dados invalidos senha errada')
            else:
                return ('Dados invalidos login errada')
    else:
        return ('vamos cadastrar')
        return True



regexRes = False
while not regexRes:
    decisao = str(input('digite 1 para logar e 2 para cadastrar'))
    regexRes = regex.number(decisao, '\\b([1-2])')
    if regexRes != True:
        print(regexRes)
        regexRes = False
try:
    resultado = mysql.selectBD('select * from cadastros')



except:
    print('erro ao conectar o bando de dados consultar o administrador')
