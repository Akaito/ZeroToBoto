# hello-python-complete.py

def write_tests(address):
    print "ping -n 5 -a " + address
    print "tracert" + address

write_tests("10.0.20.5")
write_tests("192.168.100.42")

