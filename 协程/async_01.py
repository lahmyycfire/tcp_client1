import asyncio
import threading


# 3.5 之前的协程版本
# @asyncio.coroutine
# def hello():
#     print('hello begin')
#     r = yield from asyncio.sleep(1)
#     print('hello end')

# 3.5之后的协程版本
async def hello():
    print('hello begin %s'% threading.currentThread())
    r = await asyncio.sleep(1.5)
    print('hello end  %s'% threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()