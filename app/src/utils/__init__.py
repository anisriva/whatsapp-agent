from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import List, Callable, Any
from typing import Tuple, Union


def loc_to_dot_sep(loc: Tuple[Union[str, int], ...]) -> str:
    """
    Converts a Pydantic ValidationError location tuple to a more readable path string
    i.e. ("params", "names", 1) -> 'params.names[1]'
    see https://docs.pydantic.dev/latest/errors/errors/#customize-error-messages
    for further implementation
    """
    path = ""
    for i, x in enumerate(loc):
        if isinstance(x, str):
            if i > 0:
                path += "."
            path += x
        elif isinstance(x, int):
            path += f"[{x}]"
        else:
            raise TypeError("Unexpected type")
    return path


def parallel_execute(func: Callable, items: List[Any], max_workers=3, **kwargs) -> List[Any]:
   with ThreadPoolExecutor(max_workers=max_workers) as executor:
       fn = partial(func, **kwargs)
       results = list(executor.map(fn, items))
   return results