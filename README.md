# SM-Code-Review
## Examples for SM Code Review

### [check_apache.py](https://github.com/rfreiberger/SM-Code-Review/blob/master/check_apache.py)

This is a simple script to check the status of a local web server and if the page is down, restart service. 

### [test_check_apache.py](https://github.com/rfreiberger/SM-Code-Review/blob/master/test_check_apache.py)

The unittest of the check_apache.py, this is very basic but my intention was to mock out the systems using Bottle
for the local testing of the site. 

### [bottle_admin.py](https://github.com/rfreiberger/SM-Code-Review/blob/master/bottle_admin.py)

I always liked the apache status page and wanted something where I could curl the data from a web page for other tools. 
This is a rough draft of the idea but I like to extend this to a full report tool for application status. 

