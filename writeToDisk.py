# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import codecs

print 'hi'
s = 'Foo © bar 𝌆 baz ☃ qux\n'
s2 = u'unicode str'

try:
    with codecs.open("test_output", "w", "utf-8-sig") as temp:
        temp.write("hi mom\n")
        temp.write(u"This has ♭\n")
        temp.write(s)
        temp.write(s2)
except:
    print 'failed'
