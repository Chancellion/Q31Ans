from __future__ import annotations
from dataclasses import dataclass, field
from typing import ClassVar

input("Виконав Іванченко Даніїл, КІб-1-23-4.0д")

@dataclass
class Product:
    """
    Абстрактний товар. 
    Підраховує всі свої екземпляри через class-variable total_created.
    """
    name: str
    price: float

    # class-var → спільна для всіх підкласів
    total_created: ClassVar[int] = 0

    # dataclasses не викликають __post_init__ у підкласів автоматично —
    # тож підраховуємо тут, і спадкоємці теж потраплять у статистику.
    def __post_init__(self) -> None:
        Product.total_created += 1

    # Базове «паспортне» відображення
    def info(self) -> str:
        return (f"Product: {self.name}, price = {self.price:.2f} ₴. "
                f"Total products so far: {Product.total_created}")

@dataclass
class ElectronicProduct(Product):
    warranty_period: int  # у місяцях

    def info(self) -> str:
        core = super().info()
        return f"{core}. Warranty: {self.warranty_period} months"

@dataclass
class ClothingProduct(Product):
    size: str

    def info(self) -> str:
        core = super().info()
        return f"{core}. Size: {self.size}"

if __name__ == "__main__":
    iphone = ElectronicProduct(name="iPhone 15", price=44999, warranty_period=24)
    tshirt = ClothingProduct(name="Basic T-Shirt", price=799, size="L")
    headphones = ElectronicProduct(name="Sony WH-1000XM5", price=22999, warranty_period=12)

    for item in (iphone, tshirt, headphones):
        print(item.info())
