from lxml import etree

# Пути к файлам
xml_file = "movies.xml"
dtd_file = "movies.dtd"

# Загрузка и валидация
with open(dtd_file, "r") as dtd_fp:
    dtd = etree.DTD(dtd_fp)

tree = etree.parse(xml_file)

if dtd.validate(tree):
    print("XML-документ валиден согласно DTD.")
else:
    print("Ошибки в XML-документе:")
    print(dtd.error_log.filter_from_errors())