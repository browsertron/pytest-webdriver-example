import os
import asyncio
from aiohttp import web

HOST, PORT = 'localhost', 8000

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'index.html')) as f:
    html = f.read()

def handle(request):
    return web.Response(text=html, content_type='text/html')

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    web.run_app(app, host=HOST, port=PORT)
