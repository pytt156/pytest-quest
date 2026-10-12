import pytest

from dungeon.hero import Hero
from dungeon.inventory import Inventory, Item
from dungeon.shop import Listing, Shop


@pytest.fixture
def backpack():
    return Inventory()


@pytest.fixture
def hero():
    return Hero("pytt")


@pytest.fixture
def shop():
    potion = Item("potion", 0.1, 5)
    lesser_sword = Item("lesser sword", 2, 45)
    apple = Item("apple", 1, 3)
    awesome_armor = Item("awesome armor", 50, 80)
    cooluru_ringuru = Item("cooluru ringuru", 0.1, 40)

    return Shop(
        [
            Listing(potion, 8, 10),
            Listing(lesser_sword, 100, 1),
            Listing(apple, 5, 10),
            Listing(awesome_armor, 200, 1),
            Listing(cooluru_ringuru, 60, 1),
        ]
    )


@pytest.fixture
def rich_hero(hero, shop, backpack):
    hero.gold = 500
    shop.buy(hero, backpack, "cooluru ringuru")
    return hero
