# multi-threading-simple-HTTPServer
Enable multi-threading for SimpleHTTPServer in python

Requires: Python 2 or 3.

----

In the old days the built-in Python webserver was enough to serve a local directory via HTTP, but at some point browsers became more aggressive about concurrent connections and the single-threaded `python -m SimpleHTTPServer` would just get stuck if it received two requests at once.

As a workaround, this small wrapper script enables multi-threading for SimpleHTTPServer.

# Usage
`python multi-threading-simple-HTTPServer.py`