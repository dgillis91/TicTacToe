# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:48:44 2019

@author: dgill
"""

import functools, time

current_time_millis = lambda: int(round(time.time() * 1000))

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        func_return_val = func(*args, **kwargs)
        for i in range(100):
            func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start
        print('Finished {} in {}'.format(func.__name__, run_time))
        return func_return_val
    return wrapper_timer