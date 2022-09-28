import yaml

file = open('../data/data2.yaml','r',encoding='utf-8')
value = yaml.load(stream = file,Loader=yaml.FullLoader)
print(value)
print(type(value))

