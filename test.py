# -*- coding: utf-8 -*-
from writeToDisk import *

s = 'Foo © bar 𝌆 baz ☃ qux\n'
s2 = u'unicode str\n'
s3 = "hi mom\n"
s4 = "This has ♭\n"
s5 = b"this starts with b"
lst = []
lst.append(s)
# lst.append(s2)
lst.append(s3)
lst.append(s4)
# lst.append(s5)

str = ''.join(lst)
writeToDisk('big', str)