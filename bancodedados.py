import xml.etree.ElementTree as ET
from banco import banco
# Fabio Casaroli
#Classe da função de xml ao bd

tree = ET.parse('banco.xml')
root = tree.getroot()
host = ''
user  = ''
password  = ''
db  = ''
charset  = ''


def extrairXml():
 for country in root.findall('mysql'):
  host = country.find('host').text
  user = country.find('user').text
  password = country.find('password').text
  db = country.find('db').text
  charset = country.find('charset').text
  banco.__init__(banco, host, user, password, db, charset)