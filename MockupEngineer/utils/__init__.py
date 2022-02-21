import asyncio
import functools
import random
import string

specified_keys = {"pc": 'Computers',
                  'wear': 'Wearable devices'}


def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop() \
        .run_in_executor(None,
                         functools.partial(func,
                                           *args,
                                           **kwargs))


def random_string(n: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def get_title(a: str):
    return '{}s'.format(a.title()) if a not in specified_keys.keys() else specified_keys[a]
