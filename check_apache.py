#!/usr/bin/env python
# author: Robert Freiberger
# date: 12/5/2017
# license: BSD
# notes: demo of simple sysadmin script for checking apache health

from __future__ import print_function
import re
import subprocess
import sys 

def command_run(command):
    results = subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
    stdout_value, stderr_value = results.communicate()
    if stderr_value:
        return False
    else:
        return(stdout_value)

def linux_command(system_services, action="status"):
    full_command = ("service " + system_services + " " + action)
    return(full_command)

def check_curl(curl_command_result, expected_return):
    if re.search(expected_return, curl_command_result):
        return True
    else:
        return False

def system_check(system_service, command_result):
    if command_result == "0":
        return True
    else:
        return(system_service + " failed")
        return False

def service_check_cmd(service):
    command_check = "ps aux | grep " + service + " | grep -v grep"
    return(command_check)

def main():
    # Main variables
    url_curl_command = "curl -Is http://13.57.16.129/index.html | head -1"
    url_curl = "http://13.57.16.129/index.html"
    url_return = "HTTP/1.1 200 OK"
    system_services = ['httpd']
    # Main logic
    if check_curl(command_run(url_curl_command), url_return) == True:
        print("No action taken")
        sys.exit(0)
    else:
        for services in system_services:
            if system_check(services, command_run(linux_command(services, "stop"))) == True:

                if command_run(services_check_cmd(services)) == "0":
                    return True
                else:
                    print("Services still running")
                    return False
            else:
                print("Service stop failure")
                return False
            if system_check(services, command_run(yinst_command(services, "start"))) == "0":
                if check_curl(command_run(url_curl_command), url_return) == "0":
                    print("Services are up and running")
                    return True
                else:
                    print("Services are still down, please escalate!")
                    return False

if __name__ == "__main__":
    main()
