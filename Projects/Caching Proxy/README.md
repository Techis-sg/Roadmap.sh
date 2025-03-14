# Project-URL : https://roadmap.sh/projects/caching-server

# Caching Proxy Server

A simple CLI-based caching proxy server that forwards requests to an origin server and caches responses. If the same request is made again, it serves the cached response instead of forwarding the request to the origin.

## Features
- Forwards requests to the origin server.
- Caches responses to serve repeated requests faster.
- Adds `X-Cache: HIT` or `X-Cache: MISS` headers to indicate cache status.
- Provides a command to clear the cache.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)

## Installation
Clone the repository:
```sh
git clone https://github.com/yourusername/caching-proxy.git
cd caching-proxy
```

## Setting Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

### Create and Activate Virtual Environment:
For Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
After activating the virtual environment, install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage

### Start the Proxy Server
Run the following command to start the proxy server:
```sh
python caching_proxy.py --port <port_number> --origin <origin_url>
```
Example:
```sh
python caching_proxy.py --port 3000 --origin http://dummyjson.com
```
This will start the server on `localhost:3000` and forward requests to `http://dummyjson.com`.

### Making Requests
Once the proxy server is running, open another terminal and make requests through it:
```sh
curl -i http://localhost:3000/products/1
```
- **First request:** `X-Cache: MISS` (Fetched from origin)
- **Subsequent requests:** `X-Cache: HIT` (Served from cache)

### Clearing Cache
To clear the cache, run:
```sh
python caching_proxy.py --clear-cache
```

## Troubleshooting
1. **Port Already in Use**
   - If you get an error that the port is occupied, try using a different port:
     ```sh
     python caching_proxy.py --port 4000 --origin http://dummyjson.com
     ```

2. **Connection Issues**
   - Ensure the proxy server is **running in one terminal** before making requests from another.
   - If using Git Bash or VS Code, open a **new terminal tab** to run requests.

## Adding Dependencies
If you install new dependencies, update the `requirements.txt` file:
```sh
pip freeze > requirements.txt
```

## Contributing
Feel free to submit issues or pull requests if you have any improvements!

## License
This project is licensed under the MIT License.

