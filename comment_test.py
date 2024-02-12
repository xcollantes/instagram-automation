"""Unit test for comment.py."""

import unittest
import logging
import comment


logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestComment(unittest.TestCase):
    def test_id(self):
        logging.info(comment.get_user_id("shinobu__kitsune"))
        # logging.info(comment.get_user_id("50478864266"))

    def test_page_id(self):
        logging.info(comment.get_page_id("shinobu__kitsune"))
        # logging.info(comment.get_page_id("50478864266"))

    def test_comment(self):
        pass
