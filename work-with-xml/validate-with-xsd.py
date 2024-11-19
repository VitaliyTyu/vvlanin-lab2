from lxml import etree

# Пути к файлам
xml_file = "movies.xml"
xsd_file = "movies.xsd"

# Загрузка и валидация
with open(xsd_file, "r") as xsd_fp:
    schema_root = etree.XML(xsd_fp.read())

schema = etree.XMLSchema(schema_root)
parser = etree.XMLParser(schema=schema)

try:
    etree.parse(xml_file, parser)
    print("XML-документ валиден согласно XML Schema.")
except etree.XMLSchemaError as e:
    print("Ошибки в XML-документе:", e)
