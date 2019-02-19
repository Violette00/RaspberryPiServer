import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    chunks = await websocket.recv()
    fileSize = await websocket.recv()
    print("Got Connection for ", name)
    with open('/media/pi/Pixel Drive/Media/' + name, 'wb') as f:
        count = 1
        percentage = 10
        print("Number of Chunks = %s  FileSize = %.2f MB" % (chunks, float(fileSize)))
        while True:
            data = await websocket.recv()
            if data == "Complete":
                break
            if int(chunks) > 10 and count / int(chunks) * 100 > percentage:
                print(name + " " + str(percentage) + "% complete")
                percentage += 10
            elif int(chunks) <= 10:
                print("%s %.2f%% Complete " % (name, count / int(chunks) * 100))
            if isinstance(data, str):
                f.write(data.encode())
            else:
                f.write(data)
            count += 1
    print("Done")

start_server = websockets.serve(hello, '192.168.1.150', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
