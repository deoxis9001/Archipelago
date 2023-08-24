import asyncio
import colorama
import Utils

from worlds.wl4.client import launch


if __name__ == '__main__':
    Utils.init_logging('WL4Client')
    colorama.init()
    asyncio.run(launch())
    colorama.deinit()
