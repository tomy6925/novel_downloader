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
            return []

    def Add_detail(self, section, option, value):
        cf = configparser.ConfigParser()
        try:
            cf.read(self._configFile)
            cf.add_section(section)
            cf.set(section, option, value)
            cf.set(section, 'current_url', '')
            fo = open(self._configFile, mode='w', encoding='ANSI')
            # cf.write(open(self._configFile), 'w+')
            cf.write(fo, 'w')
            fo.close()
            return True
        except Exception as ex:
            print('add_detail的error---repr(e):\t', repr(ex))
            return False

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
        except Exception as ex:
            print('Set_option的error---repr(e):\t', repr(ex))

    def Has_section(self, section):
        cf = configparser.ConfigParser()
        cf.
        try:
            cf.read(self._configFile)
            if cf.has_section(section):
                return True
            else:
                return False
        except Exception as ex:
            print('Has_section的error---repr(e):\t', repr(ex))

def test():
    print(cfg.Get_All_Section())

if __name__ == '__main__':
    cfg = MyConfig('novel.ini')
    # test()
    if cfg.Has_section('剑来'):
        print('找到section')
    else:
        print('没找到section')
    # print(cfg.Get_All_Section())
    # print(cfg.Get_option('剑来4', 'url2'))
    # print(cfg.Add_detail('剑来', 'url', 'url_detail'))

    # flag = cfg.Set_option('剑来4', 'url', 'https://www.biqubao.com/book/18370/')
    # print(flag)
    # print(cfg.Get_option('剑来4', 'url'))
    # cfg = configparser.ConfigParser()
    # cfg.read(ini_file)
    # print('读取sections是 {}'.format(cfg.sections()))
    # with open(ini_file, 'w') as fd:
    #     cfg.add_section('剑来4')
    #     cfg.set('剑来4', 'url', 'https://www.biqubao.com/book/18370/')
    #     cfg.write(fd)
    # print('sections是 {}'.format(cfg.defaults()))


