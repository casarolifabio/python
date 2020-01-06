import pymysql.cursors
import bancodedados
from bancodedados import banco


def selectBD(query):
  queryexe = query
  bancodedados.extrairXml()
  bd = bancodedados.banco
  host = str(bd.hostGet(banco))
  user = str(bd.userGet(banco))
  password =str(bd.passwordGet(banco))
  db = str(bd.dbGet(banco))
  charset = str(bd.charsetGet(banco))


  conexao = pymysql.connect(
      host = host,
      user = user,
      password = password,
      db = db,
      charset = charset,
      cursorclass = pymysql.cursors.DictCursor
     )

  cursor = conexao.cursor()
  cursor.execute(queryexe)
  result = cursor.fetchall()
  return result;

  cursor.close()
  conexao.close()

