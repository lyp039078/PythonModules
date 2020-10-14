# -*- coding: UTF-8 –*-
import logging
import re

MAX_LOG_LENGTH = 100
REPLACE_LONG_LOG = "......"
SENSITIVE_REX = r"password|session|phone(.{1,20})"
SENSITIVE_REPLACE_VALUE = "******#####*****"

def deal_msg(msg):
    """
    日志信息处理
    :param msg: 原日志信息
    :return: 处理后的日志信息
    """
    if len(msg) > MAX_LOG_LENGTH:
        msg = msg[:MAX_LOG_LENGTH] + REPLACE_LONG_LOG
    sensitive_list = re.findall(SENSITIVE_REX, msg)
    for sensitive_string in sensitive_list:
        msg = msg.replace(sensitive_string, SENSITIVE_REPLACE_VALUE)
    return msg


class SecureLoggerFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> int:
        record.msg = deal_msg(record.msg)
        return super(SecureLoggerFilter, self).filter(record)

# re.sub("[phone](.{1, 20})", "****", "this is my phone: 123456789")