import configparser
#读取环境配置
def read(path,env,option)
    conf = configparser.ConfigParser()
    conf.read(path)
    value = conf.get(env, option)
    print(value)