import argparse
import http.server
import socketserver
import requests
import hashlib
import json
from urllib.parse import urlparse

# In-memory cache
the_cache = {}

def get_cache_key(path):
    return hashlib.md5(path.encode()).hexdigest()

class CachingProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        cache_key = get_cache_key(self.path)
        
        if cache_key in the_cache:
            # Serve from cache
            self.send_response(200)
            for key, value in the_cache[cache_key]['headers'].items():
                self.send_header(key, value)
            self.send_header("X-Cache", "HIT")
            self.end_headers()
            self.wfile.write(the_cache[cache_key]['body'])
        else:
            # Forward request to the origin server
            target_url = f"{ORIGIN}{self.path}"
            response = requests.get(target_url)
            
            # Cache response
            the_cache[cache_key] = {
                'headers': dict(response.headers),
                'body': response.content
            }
            
            # Send response
            self.send_response(response.status_code)
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.send_header("X-Cache", "MISS")
            self.end_headers()
            self.wfile.write(response.content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, help="Port for the proxy server")
    parser.add_argument("--origin", type=str, help="Origin server URL")
    parser.add_argument("--clear-cache", action='store_true', help="Clear the cache")
    
    args = parser.parse_args()
    
    if args.clear_cache:
        the_cache.clear()
        print("Cache cleared successfully.")
    else:
        if not args.port or not args.origin:
            print("Error: Both --port and --origin are required.")
        else:
            ORIGIN = args.origin.rstrip('/')
            with socketserver.TCPServer(("", args.port), CachingProxyHandler) as httpd:
                print(f"Caching Proxy Server running on port {args.port}, forwarding to {ORIGIN}")
                httpd.serve_forever()
