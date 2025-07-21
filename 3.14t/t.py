#!/usr/bin/env python

import asyncio
import threading

from functools import partial

MAX_THREADS = 4

async def run(thread):
    for i in range(1500):
        print(f"[{thread} {thread.name}] Run: {i}")

def thread_target(thread):
    asyncio.run(run(thread))

threads = [threading.Thread(name=f"Thread_{i}") for i in range(MAX_THREADS+1)]

for thread in threads:
    thread._target = partial(thread_target, thread)
    thread.start()

for thread in threads:
    thread.join()
