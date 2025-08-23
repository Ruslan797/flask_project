# Задача 1: Наполнение данными
#
# Добавьте в базу данных следующие категории и продукты
# Добавление категорий:
# Добавьте в таблицу categories следующие категории:
# Название: "Электроника", Описание: "Гаджеты и устройства."
# Название: "Книги", Описание: "Печатные книги и электронные книги."
# Название: "Одежда", Описание: "Одежда для мужчин и женщин."
#
# Добавление продуктов:
# Добавьте в таблицу products следующие продукты, убедившись,
# что каждый продукт связан с соответствующей категорией:
# Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
# Название: "Ноутбук", Цена: 499.99, Наличие на складе: True, Категория: Электроника
# Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, Категория: Книги
# Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда


from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///shop.db")
Session = sessionmaker(bind=engine)
session = Session()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")

Base.metadata.create_all(engine)

# 2.

electronics = Category(name="Электроника", description="Гаджеты и устройства.")
books = Category(name="Книги", description="Печатные книги и электронные книги.")
clothes = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add_all([electronics, books, clothes])
session.commit()

products = [
    Product(name="Смартфон", price=299.99, in_stock=True, category=electronics),
    Product(name="Ноутбук", price=499.99, in_stock=True, category=electronics),
    Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=books),
    Product(name="Джинсы", price=40.50, in_stock=True, category=clothes),
    Product(name="Футболка", price=20.00, in_stock=True, category=clothes),
]
session.add_all(products)
session.commit()

# 2.
print("\nЗадача 2: Категории и продукты")
categories = session.query(Category).all()
for cat in categories:
    print(f"\nКатегория: {cat.name} ({cat.description})")
    for prod in cat.products:
        print(f"  - {prod.name}: {prod.price} $")

# 3.
print("\nЗадача 3: Обновление цены Смартфона")
smartphone = session.query(Product).filter_by(name="Смартфон").first()
if smartphone:
    smartphone.price = 349.99
    session.commit()
    print(f"Новая цена: {smartphone.price}")

# 4.
print("\nЗадача 4: Подсчет количества продуктов в категориях")
counts = (
    session.query(Category.name, func.count(Product.id))
    .join(Product)
    .group_by(Category.id)
    .all()
)
for name, cnt in counts:
    print(f"{name}: {cnt} продукт(а)")

# 5.
print("\nЗадача 5: Категории с более чем одним продуктом")
multi_products = (
    session.query(Category.name, func.count(Product.id))
    .join(Product)
    .group_by(Category.id)
    .having(func.count(Product.id) > 1)
    .all()
)
for name, cnt in multi_products:
    print(f"{name}: {cnt} продукта")
