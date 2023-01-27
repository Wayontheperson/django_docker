from __future__ import absolute_import, unicode_literals
from celery import shared_task, group, chord ,chain

@shared_task
def add(x,y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task(bind=True)
def test_func(self,n):
    result = 0
    for i in range(n):
        result+=i
    return "DONE"

def test_group(n):
    # g = group(add.s(i,i) for i in range(n))
    # result = chord(g)(xsum.s())
    
    # res = result.get()
    
    # return res
    tasks = [add.s(i,i) for i in range(n)]
    resutl = chord(tasks)(xsum.s())
    return resutl


# def test(n):
#     g = group(add.s(i,i) for i in range(n))
#     g.apply_async()
#     return g()