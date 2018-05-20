### Jqueue

Simple wrapper over 'deque' that allows:

* enqueue and dequeue methods
* initializing queue values with constructor
* passing multiple values into constructor and enqueue
* chaining enqueue() calls

`
q1 = Jqueue()
assert(len(q1) == 1)

q2 = Jqueue(1)
assert(q2.dequeue() == 1)

q3 = Jqueue(7,5,3,2,6)
assert(q3.dequeue() == 7)

q4 = Jqueue().enqueue(9).enqueue(4,3,2,1)
assert(d4.dequeue() == 9)

`
