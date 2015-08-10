# Port-Tester, firewall port testing tool

Let us suppose that during a pentest we got command execution on a remote server, but when we want to do a reverse connection to our server the connection is not established for some reason (Firewall / IPS / etc); or maybe you just want to test which ports you can access remotely from that particular server.

In that cases comes into play this simple script, which allows us to know, given a range of ports, which ports can be accessed from inside the server. We use a server that has the 65k open ports (open.zorinaq.com), and determine what ports we can access and what ports we cannot.
