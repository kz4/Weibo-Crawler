# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import codecs

def writeToDisk(filename, str):
    try:
        # "w" to overwrite, "a" to append
        with codecs.open("test_output", "a", "utf-8-sig") as file:
            file.write(str)
    except:
        print('failed')