#Из исходного текстового файла (expansion.txt)
#выбрать имена фалов, соответствующие типам:
#.xls, .xml, .html, .css, .py.Посчитать количество полученных элементов.
filename = 'ex.txt'

with open(filename, 'r',encoding='utf-8') as file:
    files = [f.strip() for f in file if f.strip().endswith(('.xls', '.xml', '.html', '.css', '.py'))]

count = len(files)

print("Список файлов с указанными расширениями:", files)
print("Количество файлов:", count)

