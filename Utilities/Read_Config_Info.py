import configparser

config = configparser.RawConfigParser()

try:
    config.read(".\\Configurations\\Config.ini")
except Exception as ex:
    print("config file got an exception", ex)


class Read_Config:

    @staticmethod
    def read_url():
        try:
            url = config.get("Common_Info", "base_url")
            print("URL: ", url)
            return url
        except Exception as ex:
            print("URL Read got an Exception", ex)

    @staticmethod
    def read_username():
        try:
            username = config.get("login", "username")
            print("username: ", username)
            return username
        except Exception as ex:
            print("username Read got an exception", ex)

    @staticmethod
    def read_password():
        try:
            password = config.get("login", "password")
            print("password: ", password)
            return password
        except Exception as ex:
            print("password got an exception: ", ex)
