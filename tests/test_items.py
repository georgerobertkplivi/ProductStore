from pages.item_details_page import ItemDetailsPage
from tests.base_test import BaseTest
from tests.enum.smart_phones import SmartphoneModel


class ItemsDetailsPageTest(BaseTest, ItemDetailsPage):

    def test_open_item_verify_details(self):

        # Go to the homepage and click on the "Phones" category
        self.goto_home()
        self.click_on_phones_category()

        # Open the "Nokia Lumia 1520" item
        item_name = SmartphoneModel.NOKIA_LUMIA_1520
        self.open_and_add_to_cart(item_name)

        # Verify the item details
        assert self.get_item_title() == item_name.value
        assert self.get_item_price() > 0  # Ensure the price is positive
        assert "Lorem ipsum" in self.get_item_description()  # Replace with the expected description text

        # Optionally, you can add more assertions here to verify other details

        # Continue with any other required tests or interactions
