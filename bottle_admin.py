#!/usr/bin/env python3

import os
import subprocess
from bottle import route, run, template


index_html = '''My web app! By {{ author }}.'''

@route('/')
def index():
    return template(index_html, author='Robert Freiberger')

@route('/uptime')
def uptime():

    completed = subprocess.run(
            ['uptime'],
            stdout=subprocess.PIPE,
    )

    return(completed.stdout.decode('utf-8'))

@route('/diskspace')
def diskspace():

    completed = subprocess.run(
            ['df -h'],
            stdout=subprocess.PIPE,
    )

    return(completed.stdout.decode('utf-8'))

@route('/cpuinfo')
def cpuinfo():

    completed = subprocess.run(
            ['cat /proc/cpuinfo'],
            stdout=subprocess.PIPE,
    )

    return(completed.stdout.decode('utf-8'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)