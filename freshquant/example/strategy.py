import os
import pandas as pd
import logging

logger = logging.getLogger('Strategy')


class Strategy:
    start_time=''
    end_time=''

    def init(self, *args, **kwargs):
        pass

    def handler_bar(self, *args, **kwargs):
        pass

    def finish_day(self, *args, **kwargs):
        pass
