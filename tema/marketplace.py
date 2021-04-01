"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock, currentThread
from typing import Dict


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.number_in_queue = queue_size_per_producer

        self.product_lock = Lock()
        self.count_producer = -1
        self.product_dict = dict()

        self.cart_lock = Lock()
        self.cart_idx = -1
        self.cons_dict = dict()

        self.printer = Lock()

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        self.product_lock.acquire()
        self.count_producer += 1
        self.product_dict[self.count_producer] = []
        self.product_lock.release()
        return self.count_producer

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace
        :returns True or False. If the caller receives False, it should wait and then try again.
        # """
        if len(self.product_dict[int(producer_id)]) < self.number_in_queue:
            self.product_dict[int(producer_id)].append(product)
            return True
        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.cart_lock.acquire()
        self.cart_idx += 1
        self.cons_dict[self.cart_idx] = []
        self.cart_lock.release()
        return self.cart_idx

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for i in range(0, len(self.product_dict)):
            # value of the key
            if product in self.product_dict[i]:
                self.product_dict[i].remove(product)
                self.cons_dict[cart_id].append(product)
                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        if product in self.cons_dict[cart_id]:
            self.cons_dict[cart_id].remove(product)
            self.product_dict[0].append(product)

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        for x in self.cons_dict[cart_id]:
            self.printer.acquire()
            print(currentThread().getName() + " bought " + str(x))
            self.printer.release()
