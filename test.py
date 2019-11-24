import os
import configparser

#
# def config_init(ini_file):
#     fn = ini_file
#     if not os.path.isfile(fn):
#         fo = open(ini_file, mode='w', encoding='ANSI')
#         fo.close()
#
# def config_has_section():
# # def config_get():
# #
# #
# #
# # def config_set():

class MyConfig:
    _configFile=''
    def __init__(self, ini_path):
        self._configFile = ini_path
        if not os.path.isfile(self._configFile):
            fo = open(self._configFile, mode='w', encoding='ANSI')
            fo.close()

    def Get_All_Section(self):
        cf = configparser.ConfigParser()
        try:
            cf.read(self._configFile)
            all_sections = cf.sections()
            return all_sections
        except:
            return ''

    def Get_option(self, section, option):
        cf = configparser.ConfigParser()
        try:
            cf.read(self._configFile)
            rep_option = cf.get(section, option)
            return rep_option
        except:
            return '没有找到'

    def Set_option(self, section, option, value):
        cf = configparser.ConfigParser()
        try:
            cf.read(self._configFile)
            cf.set(section, option, value)
            cf.write(open(self._configFile, 'w'))
            return 'ok'
        except:
            return 'error'


if __name__ == '__main__':
    cfg = MyConfig('novel.ini')
    print(cfg.Get_All_Section())
    print(cfg.Get_option('剑来4', 'url'))
    flag = cfg.Set_option('剑来4', 'url', '1333311')
    print(flag)
    print(cfg.Get_option('剑来4', 'url'))
    # cfg = configparser.ConfigParser()
    # cfg.read(ini_file)
    # print('读取sections是 {}'.format(cfg.sections()))
    # with open(ini_file, 'w') as fd:
    #     cfg.add_section('剑来4')
    #     cfg.set('剑来4', 'url', 'https://www.biqubao.com/book/18370/')
    #     cfg.write(fd)
    # print('sections是 {}'.format(cfg.defaults()))


