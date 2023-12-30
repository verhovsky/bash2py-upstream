#! /usr/bin/env python
from __future__ import print_function
import glob
def Glob(value):
  ret = glob.glob(value)
  if len(ret) < 1:
    ret = [ value ]
  return ret

print(Glob("--without-http_autoindex_module"),Glob("--without-http_ssi_module"),Glob("--without-http_userid_module"),Glob("--without-http_auth_basic_module"),Glob("--without-http_geo_module"),Glob("--without-http_fastcgi_module"),Glob("--without-http_empty_gif_module"),Glob("--with-openssl=/lib64"))
