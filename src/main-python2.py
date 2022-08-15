#!/usr/bin/python
import argparse
import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import sys

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port", type = int, nargs = "?",
        action = "store", default = 8000,
        help = "Specify alternate port [default: 8000]",
    )
    parser.add_argument(
        "--iface", type = str, nargs = "?",
        action = "store", default = "127.0.0.1",
        help = "Specify iface [default: 127.0.0.1]",
    )
    args = parser.parse_args(argv[1:])
    server_address = (args.iface, args.port)
    srv = ThreadedHTTPServer(server_address, SimpleHTTPServer.SimpleHTTPRequestHandler)
    sa = srv.socket.getsockname()
    print "Serving http://%s:%r ..." % (sa[0], sa[1])
    srv.serve_forever()

if __name__ == "__main__":
    sys.exit(main(sys.argv))