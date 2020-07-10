import os
import pandas as pd
import logging

logger = logging.getLogger('Strategy')

class Strategy:
    start_time=''
    end_time=''

    def init(self, *args, **kwargs):
        pass

    def handler_data(self, *args, **kwargs):
        pass

    def finish(self, *args, **kwargs):
        pass