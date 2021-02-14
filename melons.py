"""Classes for melon orders."""

import random
import datetime


today = datetime.date.today()

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = None
    
    def get_base_price(self, min_price=5, max_price=10):

        surcharge = 0

        # current_date = datetime.date.today().weekday()

        now = datetime.datetime.now()

        if  now.weekday() < 5 and now[3] < 12 and now[3] > 8:
            surcharge = self.qty * 4


        base_price = random.randint(min_price, max_price)
        return base_price + surcharge


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = 1.5 * base_price
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "international"
        self.country_code = country_code
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""
        
        if self.qty < 10:
            return super().get_total() + 3
        else:
            return super().get_total()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
    
