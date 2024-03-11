import configparser
config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class Readconfig:

    @staticmethod
    def getAppurl():
        url = config.get('Common data', 'baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('Common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common data', 'password')
        return password
