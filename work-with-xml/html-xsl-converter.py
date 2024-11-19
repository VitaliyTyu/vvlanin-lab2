from lxml import etree  # Для работы с XML и XSLT

# Пути к файлам
xml_file = "movies.xml"  # Исходный XML-файл
xslt_file = "movies_to_html.xsl"  # XSLT-файл для преобразования
output_file = "movies.html"  # Результирующий HTML-файл

# Загрузка исходного XML в dom
dom = etree.parse(xml_file)

# Загрузка XSLT
xslt = etree.parse(xslt_file)

# Преобразование
transform = etree.XSLT(xslt)  # Создание трансформации
result = transform(dom)  # Применение трансформации к XML

# Сохранение результата в файл
with open(output_file, "wb") as f:
    f.write(str(result).encode("utf-8"))

print("XSLT-преобразование в HTML завершено. Сохранено в", output_file)