# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:27:20 2019

@author: dgill
"""

class Event:
    pass

class Observable:
    def __init__(self):
        self._callbacks = []
    
    def subscribe(self, callback):
        self._callbacks.append(callback)
        
    def fire(self, **kwargs):
        e = Event()
        e.source = self
        for k, v in kwargs.items():
            setattr(e, k, v)
        for func in self._callbacks:
            func(e)