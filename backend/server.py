import aiohttp_cors as aiohttp_cors
from aiohttp import web
import uvloop
import asyncio
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def hello(request):
    data = {'hello': 'you devilish data'}
    return web.json_response(data=data)

async def calculate(request):

    data = await request.post()
    data= dict(data)
    val1 = int(data['var1'])
    val2 = int(data['var2'])
    result = {'result': operator_mapping(data['operator'])(val1,val2)}
    return web.json_response(data = result)

def operator_mapping(op):

    operators = {
        '/': int.__truediv__,
        'mod': int.__mod__,
        'x': int.__mul__,
        '+': int.__add__,
        '-': int.__sub__
    }
    return operators[op]

app = web.Application()
app.router.add_get('/', hello)
app.router.add_post('/',calculate)

def allow_all_cors():

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)

allow_all_cors()
web.run_app(app)