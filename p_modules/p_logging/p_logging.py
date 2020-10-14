# -*- coding: UTF-8 –*-
import logging
import re

MAX_LOG_LENGTH = 100
REPLACE_LONG_LOG = "......"
SENSITIVE_REX = "[password|session|phone](.{1,20})"
SENSITIVE_REPLACE_VALUE = "******#####*****"

def deal_msg(msg):
    """
    日志信息处理
    :param msg: 原日志信息
    :return: 处理后的日志信息
    """
    if len(msg) > 100:
        msg = msg[:MAX_LOG_LENGTH] + REPLACE_LONG_LOG
    msg = re.sub(SENSITIVE_REX, SENSITIVE_REPLACE_VALUE, msg)
    return msg


class SecureLoggerFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> int:
        record.msg = deal_msg(record.msg)
        return super(SecureLoggerFilter, self).filter(record)

# re.sub("[phone](.{1, 20})", "****", "this is my phone: 123456789")