# Парсинг файла data_description
def parse_data_description(file):
    with open(file) as f:
        lines = f.readlines()

    # Словарь из параметр: список значений
    params_values_dict = {}
    for line in lines:
        words = line.split()

        if words:
            word1 = words[0]
        else:
            continue

        if ':' in word1:
            param = word1[:-1]
            vals = []
            params_values_dict[param] = vals
        else:
            words = line.split("\t")
            word1 = words[0].strip()

            if word1.strip() == "NA":
                word1 = "NA=" + " ".join(words[1:])
                word1 = word1.replace('\n', '')

            # Скорректируем тип для числовых значений
            if param in ['MSSubClass', 'OverallQual', 'OverallCond']:
                word1 = int(word1)

            # Скорректируем опечатки
            if param == 'BldgType':
                if word1 == 'Duplx':
                    word1 = 'Duplex'
                if word1 == '2FmCon':
                    word1 = '2fmCon'

            if param == 'Neighborhood':
                if word1 == 'Names':
                    word1 = 'NAmes'

            vals.append(word1)

    # удалим параметры, у которых нет значений
    to_del = []
    for param in params_values_dict:
        if not params_values_dict[param]:
            to_del.append(param)

    for param in to_del:
        del params_values_dict[param]

    return params_values_dict

# descriptions_values = parse_data_description(data_description_file)