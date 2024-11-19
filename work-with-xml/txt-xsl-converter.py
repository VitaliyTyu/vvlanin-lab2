from lxml import etree

# Пути к файлам
xml_file = "movies.xml"
xslt_file = "movies_to_txt.xsl"
output_file = "movies.txt"

# Преобразование
dom = etree.parse(xml_file)
xslt = etree.parse(xslt_file)
transform = etree.XSLT(xslt)

result = transform(dom)

# Сохранение результата
with open(output_file, "wb") as f:
    f.write(str(result).encode("utf-8"))

print("XSLT-преобразование в текст завершено. Сохранено в movies.txt.")
