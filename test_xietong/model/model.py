from sqlalchemy import Column, String, create_engine, BigInteger, DateTime, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class InvoiceGoodsType(Base):
    # 表的名字:
    __tablename__ = 'gt_invoice_goods_type'

    # 表的结构:
    id = Column(BigInteger(), primary_key=True)
    create_time = Column(DateTime())
    merchant_id = Column(String(11))
    update_time = Column(DateTime())
    version = SmallInteger()
    code = Column(String(30))
    enterprise_id = Column(BigInteger())
    is_leaf = Column(SmallInteger())
    name = Column(String(60))
    parent_id = Column(BigInteger())

    def __repr__(self):
        return "{name:%s, code:%s}" % (self.name, self.code)
