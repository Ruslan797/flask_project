# Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.

# from sqlalchemy import create_engine
#
# engine = create_engine("sqlite:///:memory:", echo=True)

# Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.

# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# session = Session()

# Задача 3: Определите модель продукта Product со следующими типами колонок:
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# price: числовое значение с фиксированной точностью
# in_stock: логическое значение

# from sqlalchemy import Column, Integer, String, Numeric, Boolean
# from sqlalchemy.orm import declarative_base
#
# Base = declarative_base()
#
# class Product(Base):
#     __tablename__ = 'products'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     price = Column(Numeric(10, 2), nullable=False)
#     in_stock = Column(Boolean, default=True)


# Задача 4: Определите связанную модель категории Category со следующими типами колонок:
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# description: строка (макс. 255 символов)

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
#
# class Category(Base):
#     __tablename__ = 'categories'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     description = Column(String(255))


# Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id.

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship, DeclarativeBase
#
# class Base(DeclarativeBase):
#     pass
#
# class Category(Base):
#     __tablename__ = "categories"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     description = Column(String(255))
#
#     products = relationship("Product", back_populates="category")
#
# class Product(Base):
#     __tablename__ = "products"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     category_id = Column(Integer, ForeignKey("categories.id"))
#
#     category = relationship("Category", back_populates="products")


