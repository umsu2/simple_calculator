from aiohttp import web
import uvloop
import asyncio
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def hello(request):
    data = {'hello': 'you devilish data'}
    return web.json_response(data=data)


app = web.Application()
app.router.add_get('/', hello)

web.run_app(app)