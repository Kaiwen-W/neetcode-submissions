from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks: # O(n)
            freq[t] += 1 
        
        tasks_freq = [
            [-freq, task] for task, freq in freq.items()
        ] # max-heap

        heapq.heapify(tasks_freq) # O(n) 

        q = deque() # Will store pairs: [remaining_frequency, ready_time]
        time = 0

        while tasks_freq or q:
            time += 1 # 1 unit of time passes
            
            if tasks_freq:
                # Pop the most frequent task
                freq, task = heapq.heappop(tasks_freq)
                
                # We "schedule" it by adding 1 (since your frequencies are negative in the max-heap)
                freq += 1
                
                # If it still needs to be scheduled again, put it in the waiting room
                if freq < 0:
                    ready_time = time + n
                    q.append([freq, ready_time, task])
                    
            # Now check if the task at the front of the queue is ready to come out
            if q and q[0][1] == time:
                # It's done cooling down! Put it back into the max-heap
                ready_task = q.popleft()
                heapq.heappush(tasks_freq, [ready_task[0], ready_task[2]])
        
        return time
