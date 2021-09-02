import filter
import os

for pyf in filter.python_files:
    p_stmt = None # i don't know how to covert .py to .pyo
    os.system(p_stmt+pyf)
    os.remove(pyf)
    os.rename(pyf+"o",pyf)


def encrypt_html(html):
    return None # IDK again

def encrypt_css(css):
    return None # IDK again

def encrypt_js(js):
    return None # IDK again

for htf in filter.html_files:
    encrypt_html(htf)

for cf in filter.css_files:
    encrypt_css(cf)

for jf in filter.js_files:
    encrypt_js(jf)