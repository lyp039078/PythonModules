import configparser

config_parser = configparser.ConfigParser()

config_parser.read("l_config.ini", encoding="utf-8")

print(config_parser.sections())
print(config_parser.get("Flask", "debug"))