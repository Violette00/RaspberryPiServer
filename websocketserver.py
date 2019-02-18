import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("Got Connection for ", name)
    with open("Recv " + name, 'wb') as f:
        while True:
            data = await websocket.recv()
            if data == "Complete":
                break
            f.write(data)
    print("Done")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()