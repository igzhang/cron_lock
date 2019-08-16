# -*- coding: utf-8 -*-
"""
unit test file
@author: fallthrough
"""
import unittest
import time
import threading
from cron_lock import CountLock


class TestCountLock(unittest.TestCase):

    def test_count(self):
        second_test = 10
        time_pool = []
        thread_pool = []
        lock = CountLock(count=30, seconds=second_test)
        for i in range(60):
            o = threading.Thread(target=self.func_for_test, args=(lock, time_pool,))
            o.start()
            thread_pool.append(o)
        for i in thread_pool:
            i.join()
        self.assertEqual(len(time_pool), 60)

    def func_for_test(self, lock, time_pool):
        lock.acquire()
        time_pool.append(time.time())

    def test_time(self):
        second_test = 10
        time_pool = []
        thread_pool = []
        lock = CountLock(count=30, seconds=second_test)
        for i in range(60):
            o = threading.Thread(target=self.func_for_test, args=(lock, time_pool,))
            o.start()
            thread_pool.append(o)
        for i in thread_pool:
            i.join()
        time_pool.sort()
        period = time_pool[-1] - time_pool[0]
        print("耗时", period)
        self.assertGreaterEqual(period, 10)
        self.assertLessEqual(period, 11)
