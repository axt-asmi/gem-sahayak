#!/usr/bin/env python3
"""Static server for the GeM Sahayak site that never lets the browser cache.

Plain `python3 -m http.server` sends Last-Modified, so browsers keep serving
stale copies of index.html / i18n.js after an edit. This subclass sends
no-store on every response so a normal reload always shows current files.
"""
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8777
    directory = sys.argv[2] if len(sys.argv) > 2 else "."
    handler = partial(NoCacheHandler, directory=directory)
    with ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print("Serving %s at http://localhost:%d (no-cache)" % (directory, port))
        httpd.serve_forever()
