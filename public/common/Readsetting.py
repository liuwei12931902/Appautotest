import configparser


# ****************************************
#  使用方法
# DoSetting  = ReadSetting(setting.ini)
# DoSetting.getsettingvalues(section,name)
# ***************************************


class ReadSetting(object):

    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getsettingvalues(self, section, name):
        value = self.cf.get(section, name)
        return value

