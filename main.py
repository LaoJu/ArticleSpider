# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: LaoJu
# @Date  : 2019/1/30
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","jobbole"])
execute(["scrapy","crawl","lagou"])

