import configparser
import os

conf = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/cfg.ini")
print(config_path)
conf.read(config_path, encoding="utf-8")
print(conf.sections())
db_url = conf.get("db", 'conn')
print(db_url)

