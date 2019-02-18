import asyncio
import websockets

async def hello():
    async with websockets.connect(
        'ws://localhost:8765') as websocket:
        name = "VID_20180912_202454.mp4"

        await websocket.send(name)
        f = open(name, 'rb')
        l = f.read(1024)
        while (l):
            await websocket.send(l)
            l = f.read(1024)
        await websocket.send("Complete")
        f.close()

asyncio.get_event_loop().run_until_complete(hello())