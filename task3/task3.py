import json

values_sl = {}

with open("values.json") as read_file:
    values_json = json.load(read_file)

values_json = (values_json['values'])

# Цикл записывает значения в пустой словарь для удобства в дальнейшей работе
for i in values_json: 
    id_ = i.get('id')
    value = i.get('value')
    values_sl.update({id_: value})

with open("tests.json") as read_file:
    tests_json = json.load(read_file)

tests_json = (tests_json['tests'])


# Функция позволяет изменить значение "value" в соответствие с "id" во вложенном словаре, если он содержит "values", функция вызывает себя и переходит на следующий уровень вложенности
def nextDict(cont): 
	for slov in cont:
	    if slov["id"] in values_sl:
	        slov["value"] = values_sl.get(slov["id"])
	    else:
	        pass
	    if "values" in slov:
	        cont = slov["values"]
	        nextDict(cont)

# Цикл изменяет значение "value", запускает функцию nextDict(), если в словаре есть значение "values"
for sl in tests_json: 
	sl['value'] = values_sl.get(sl['id'])
	if 'values' in sl:
		cont = sl['values']
		nextDict(cont)

with open("report.json", "w", encoding="utf-8") as file:
    json.dump(tests_json, file, indent = 2)
