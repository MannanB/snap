from .api import *
from . import cache
from . import httpreq
import asyncio

# adjust polices

# honestly idk what to do here until i try cross platform :)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
