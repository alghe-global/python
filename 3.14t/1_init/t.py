#!/usr/bin/env python

import os
import asyncio

async def run():
    return await asyncio.to_thread(os.urandom, 1500)

asyncio.run(run())
