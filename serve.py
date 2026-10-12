#!/usr/bin/env python3
"""Serve this app on a consistent, loopback-only browser origin."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import argparse
import subprocess
import sys
import threading
import webbrowser

parser = argparse.ArgumentParser()
parser.add_argument('--no-open', action='store_true')
args = parser.parse_args()
url = 'http://localhost:8765/'
handler = partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).resolve().parent))
try:
    server = ThreadingHTTPServer(('127.0.0.1', 8765), handler)
except OSError as error:
    sys.exit(f'Cannot start the app on port 8765: {error}. Close the earlier launcher and try again.')

def open_app():
    if sys.platform == 'darwin':
        result = subprocess.run(['open', '-a', 'Google Chrome', url], capture_output=True)
        if result.returncode == 0:
            return
    webbrowser.open(url)

if not args.no_open:
    threading.Timer(.5, open_app).start()
print(f'Magic Caster Wand: {url}\nKeep this window open. Press Ctrl+C to stop.', flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
