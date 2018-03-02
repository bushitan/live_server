# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from lite.query.company import *


class ActionCompany():
    def __init__(self):
        self.query_company = QueryCompany()
    def GetCompanyInfo(self):
        return self.query_company.Get()

if __name__ == "__main__":
    a = ActionCompany()
    print a.GetCompanyInfo()















