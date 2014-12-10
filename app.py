#!/usr/bin/env python
'''
app.py
'''

from erddap_management import app
from erddap_management.config import Host, Port, Debug

if __name__ == '__main__':
    app.run(host=Host, port=Port, debug=Debug)
