#  -*- coding: UTF-8 –*-
#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import logging
import unittest

from p_modules.p_logging import p_logging
from p_modules.p_logging.p_logging import SecureLoggerFilter


class SecureLoggerFilterTest(unittest.TestCase):
    def test_log_msg(self):
        msg = "this is my phone: 123456789, call me"
        logger = logging.getLogger(__name__)
        logger.addFilter(SecureLoggerFilter())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.info(msg)
        # self.assertEqual(True, False)

    def test_deal_msg(self):
        msg = "this is my phone: 123456789, call me"
        res_msg = p_logging.deal_msg(msg)
        self.assertNotEqual(msg, res_msg)
        self.assertNotIn(p_logging.SENSITIVE_REPLACE_VALUE, msg)
        self.assertIn(p_logging.SENSITIVE_REPLACE_VALUE, res_msg)

    def test_to_long_log(self):
        msg = "this is the file path : E:/Project/PythonModules/p_test/p_logging/p_logging.py in E:\Project\PythonModules\p_test\p_logging "
        print(len(msg))
        self.assertGreater(len(msg), p_logging.MAX_LOG_LENGTH)
        res_msg = p_logging.deal_msg(msg)
        self.assertIn(p_logging.REPLACE_LONG_LOG, res_msg)


if __name__ == '__main__':
    unittest.main()
