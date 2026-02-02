"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False
"""
    JUSTIFICATION:
    I chose a set data structure because it provides O(1) average-case lookup time.
    As we iterate through the list (O(n)), we check membership and add to the set,
    giving us overall O(n) time complexity - much better than O(n²) nested loops.
    """


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self._items = []

    def add_task(self, task):
        self._items.append(task)

    def remove_oldest_task(self):
        if not self._items:
            return None
        return self._items.pop(0)
"""
    JUSTIFICATION:
    I chose a Python list (deque-like usage) because this is a classic FIFO queue pattern.
    add_task() performs an append operation which is O(1), and remove_oldest_task() 
    uses pop(0) which is O(n). For better performance, collections.deque could be used
    with popleft() for O(1) removal, but a list works for basic implementation.
    """

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self._seen = set()

    def add(self, value):
        self._seen.add(value)

    def get_unique_count(self):
        return len(self._seen)
"""
    JUSTIFICATION:
    I chose a set data structure because sets automatically maintain uniqueness and
    provide O(1) add operations. The get_unique_count() simply returns len() which is O(1).
    This gives us optimal performance for tracking unique values in a stream.
    """