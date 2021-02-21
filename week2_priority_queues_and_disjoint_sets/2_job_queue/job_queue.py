import heapq            
class Worker:
    def __init__(self, worker_index, start_time = 0):
        self.worker_index = worker_index
        self.start_time = start_time
    
    def __lt__(self, other):
        if self.start_time == other.start_time:
            return self.worker_index < other.worker_index
        return self.start_time < other.start_time
    
    def __gt__(self, other):
        if self.start_time == other.start_time:
            return self.worker_index > other.worker_index
        return self.start_time > other.start_time
    
    def add_start_time(self, job):
        self.start_time += job
        return self    
    
    def __repr__(self):
        return f"{self.worker_index} {self.start_time}"    

def assign_jobs(n_workers, jobs):
    workerQ = [Worker(i) for i in range(n_workers)]

    for job in jobs:
        worker = heapq.heappop(workerQ)
        print(worker)
        next = worker.add_start_time(job)
        heapq.heappush(workerQ, worker)
        
        
def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)


if __name__ == "__main__":
    main()
        
    
     