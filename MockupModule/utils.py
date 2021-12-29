import asyncio
import functools
import random
import string

from FlowyModule.models import Track


def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop() \
        .run_in_executor(None,
                         functools.partial(func,
                                           *args,
                                           **kwargs))


def random_string(n: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def prepare_name(name: str):
    symbols = '-1234567890qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'
    return "".join([a if a.lower() in symbols else "-" for a in name])


def gen_track_name(element: Track, container: str):
    return '{}-{}-{}.{}'.format(prepare_name(element.artists[0].name),
                                prepare_name(element.title[:15]),
                                random_string(6), container)