#!/usr/bin/env python

import unittest
import sys
from check_apache import *

class check_apacheTestCase(unittest.TestCase):

    """These are testing the Subprocess.Popen function"""

    @unittest.skipUnless(sys.platform.startswith("linux"), "Requires Linux")
    def test_command_linux(self):
        command_string = command_run("uname")
        self.assertEqual(command_string, "Linux\n")

    @unittest.skipUnless(sys.platform.startswith("linux"), "Requires Linux")
    def test_command_linux_fail(self):
        command_string = command_run("echo 'foo' 2>&1")
        self.assertIn(command_string, "foo\n")

    @unittest.skipUnless(sys.platform.startswith("darwin"), "Requires Mac")
    def test_command_mac(self):
        command_string = command_run("uname")
        self.assertEqual(command_string, "Darwin\n")

    @unittest.skipUnless(sys.platform.startswith("darwin"), "Requires Mac")
    def test_command_mac_fail(self):
        command_string = command_run("echo 'foo' 2>&1")
        self.assertEqual(command_string, "foo\n")

    """Testing the functions of the script"""

    def test_yinst_command(self):
        command_string = yinst_command("yapache", "start")
        self.assertEqual(command_string, "yinst start yapache")

    def test_linux_command(self):
        command_string = linux_command("httpd", "start")
        self.assertEqual(command_string, "service httpd start")

    def test_linux_command_2(self):
        command_string = linux_command("foo")
        self.assertEqual(command_string, "service foo status")

    def test_check_curl(self):
        command_string = check_curl("foo", "foo")
        self.assertEqual(command_string, "No action taken")

    def test_check_curl_2(self):
        test_string = """
        HTTP/1.1 200 OK
        Server: nginx/1.10.3
        Date: Thu, 09 Feb 2017 22:02:27 GMT
        Content-Type: text/html
        Content-Length: 588
        Connection: keep-alive
        Last-Modified: Fri, 09 Dec 2016 07:49:22 GMT
        Accept-Ranges: bytes
        """ 
        command_string = check_curl(test_string, "HTTP/1.1 200 OK")
        self.assertEqual(command_string, "No action taken")

    def test_check_curl_fail(self):
       test_string = """
       HTTP/1.1 404 Not Found
       Server: nginx/1.10.3
       Date: Thu, 09 Feb 2017 22:08:48 GMT
       Content-Type: text/html
       Content-Length: 4250
       Connection: keep-alive
       Last-Modified: Wed, 10 Aug 2016 00:07:41 GMT
       Accept-Ranges: bytes
       """
       command_string = check_curl(test_string, "HTTP/1.1 404 Not Found")
       self.assertEqual(command_string, "No action taken")

    def test_system_check(self):
        command_string = system_check("apache", "0")
        self.assertEqual(command_string, "0")

    def test_system__check_fail(self):
        command_string = system_check("foo", "1")
        self.assertEqual(command_string, "foo failed")

unittest.main()
