import random

from pages.homepage import HomePage
from tests.enum.laptops import LaptopModel
from tests.enum.smart_phones import SmartphoneModel


class ItemDetailsPage(HomePage):
    ITEM_TITLE = ".name"
    ITEM_PRICE = ".price-container"
    ITEM_DESCRIPTION = "div[id='more-information'] p"
    ADD_TO_CART_BUTTON = ".btn.btn-success.btn-lg"

    def get_item_title(self):
        return self.get_text(self.ITEM_TITLE)

    def get_item_price(self):
        price_text = self.get_text(self.ITEM_PRICE)
        price_integer = int(price_text.replace("$", "").split()[0])
        return price_integer

    def get_item_description(self):
        return self.get_text(self.ITEM_DESCRIPTION)

    def click_add_to_cart_button(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def open_and_add_to_cart(self, item_name):
        # Go to the homepage
        self.goto_home()

        # Open the specified item and add it to the cart
        self.open_item(item_name)
        item_details_page = ItemDetailsPage(self.driver)
        item_details_page.click_add_to_cart_button()

    def add_items_to_cart(self, num_items):
        # Go to the homepage
        self.goto_home()

        # Combine items from SmartphoneModel and LaptopModel enums
        all_smartphones = [model.value for model in SmartphoneModel]
        all_laptops = [model.value for model in LaptopModel]
        all_items = all_smartphones + all_laptops

        # Randomly select the specified number of items from the list
        selected_items = random.sample(all_items, num_items)

        # Open and add each item to the cart
        for item_name in selected_items:
            self.open_item(item_name)
            item_details_page = ItemDetailsPage(self.driver)
            item_details_page.click_add_to_cart_button()

    def open_nokia_lumia_1520_and_add_to_cart(self):
        # Go to the homepage and click on the "Phones" category
        self.goto_home()
        self.click_on_phones_category()

        # Open the "Nokia Lumia 1520" item
        item_name = SmartphoneModel.NOKIA_LUMIA_1520.value
        self.open_item(item_name)

        # Add the item to the cart
        item_details_page = ItemDetailsPage(self.driver)
        item_details_page.click_add_to_cart_button()
