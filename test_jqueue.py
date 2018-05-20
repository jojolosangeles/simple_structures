import pytest

from jqueue import Jqueue

def test_empty():
    q = Jqueue()
    assert(len(q) == 0)

def test_enqueue():
    q = Jqueue()
    q.enqueue(1)
    q.enqueue(22)
    q.enqueue(333)
    q.enqueue(4444)
    q.enqueue(55555)
    assert(len(q) == 5)
    assert(q.dequeue() == 1)
    assert(len(q) == 4)
    assert(q.dequeue() == 22)
    assert(len(q) == 3)
    assert(q.dequeue() == 333)
    assert(len(q) == 2)
    assert(q.dequeue() == 4444)
    assert(len(q) == 1)
    assert(q.dequeue() == 55555)

def test_fluent():
    q = Jqueue().enqueue(1).enqueue(2).enqueue(3)
    assert(q.dequeue() == 1)
    assert(q.dequeue() == 2)
    assert(q.dequeue() == 3)

def test_multiple_args():
    q = Jqueue().enqueue(1,2,3)
    assert(q.dequeue() == 1)
    assert(q.dequeue() == 2)
    assert(q.dequeue() == 3)

def test_zero_constructor_args():
    q = Jqueue()
    assert(len(q) == 0)

def test_one_constructor_arg():
    q = Jqueue(7)
    assert(q.dequeue() == 7)

def test_multiple_constructor_args():
    q = Jqueue(3,1,5,7,9)
    assert(q.dequeue() == 3)
    assert(q.dequeue() == 1)
    assert(q.dequeue() == 5)
    assert(q.dequeue() == 7)
    assert(q.dequeue() == 9)