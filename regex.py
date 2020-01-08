import re
#Biblioteca de Regex
# Fabio Casaroli
# Regex Number
def number(numero, regex):
    try:
        numbers = re.match(regex, numero) # Regex Number 1 a 2
        if numbers == None:
            return ('dado invalido por favor selecionar um do menu solicitado')
        else:
            return True
    except:
      return False
