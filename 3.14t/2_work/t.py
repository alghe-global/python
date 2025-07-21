#!/usr/bin/env python

import os
import asyncio

async def run():
    return await asyncio.to_thread(os.urandom, 1500)

async def work():
    tasks = [run() for _ in range(3000)]
    await asyncio.gather(*tasks)

asyncio.run(work())
