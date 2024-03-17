from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

        

    def ping(self, t: int) -> int:
        # Add the new request time to the queue
        self.queue.append(t)

        # Remove all requests that are older than 3000 milliseconds from 't'
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # The remaining elements in the queue are the requests within [t-3000, t]
        return len(self.queue)