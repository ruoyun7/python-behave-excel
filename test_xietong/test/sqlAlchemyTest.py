from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

from model.model import InvoiceGoodsType

# 初始化数据库连接:
import configparser
import os

conf = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/cfg.ini")
print(config_path)
conf.read(config_path, encoding="utf-8")
print(conf.sections())
db_url = conf.get("db", 'conn')
print(db_url)
engine = create_engine(db_url)
# 创建DBSession类型:
session = sessionmaker(bind=engine)
session = session()
print(session.query(InvoiceGoodsType).filter_by(code="100001").first())
print(session.query(InvoiceGoodsType).filter(InvoiceGoodsType.name.like("%1%")).all())
print(session.query(InvoiceGoodsType).filter(InvoiceGoodsType.name.like("%1%"), InvoiceGoodsType.name == "312").all())
