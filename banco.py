class banco(object):
    def __init__(self, host, user, password, db, charset):
        self.__host = host
        self.__user = user
        if password == None:
            self.__password = ''
        else:
            self.__password = password
        self.__db = db
        self.__charset = charset

    def hostGet(self):
        return self.__host

    def hostSet(self, host):
        self.__host = host

    def userGet(self):
        return self.__user

    def userSet(self, user):
        self.__user = user

    def passwordGet(self):
        return self.__password

    def passwordSet(self, password):
        self.__password = password

    def dbGet(self):
        return self.__db

    def dbSet(self, db):
        self.__db = db

    def charsetGet(self):
        return self.__charset

    def charsetSet(self, charset):
        self.__charset = charset

