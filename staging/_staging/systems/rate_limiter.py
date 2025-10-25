import time
import threading
from collections import deque, defaultdict
from typing import Dict, Optional, List
import math

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                return True
            
            return False

class RateLimiterOptimized:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.stats = {
            'allowed': 0,
            'blocked': 0,
            'total': 0
        }
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                self.stats['allowed'] += 1
                self.stats['total'] += 1
                return True
            else:
                self.stats['blocked'] += 1
                self.stats['total'] += 1
                return False
    
    def get_stats(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()

class RateLimiterWithValidation:
    def __init__(self, max_requests: int, time_window: int):
        if max_requests <= 0 or time_window <= 0:
            raise ValueError("max_requests and time_window must be positive")
        
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
    
    def is_allowed(self, identifier: str = "default") -> bool:
        if not identifier or not isinstance(identifier, str):
            return False
        
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                return True
            
            return False

class RateLimiterWithConstraints:
    def __init__(self, max_requests: int, time_window: int, constraints):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.constraints = constraints
    
    def is_allowed(self, identifier: str = "default") -> bool:
        if not self.constraints(identifier):
            return False
        
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                return True
            
            return False

class RateLimiterWithOptimization:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.last_cleanup = time.time()
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            if current_time - self.last_cleanup > self.time_window:
                while self.requests and self.requests[0] <= current_time - self.time_window:
                    self.requests.popleft()
                self.last_cleanup = current_time
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                return True
            
            return False

class RateLimiterWithAdvancedOptimization:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.last_cleanup = time.time()
        self.cleanup_interval = time_window / 2
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            if current_time - self.last_cleanup > self.cleanup_interval:
                while self.requests and self.requests[0] <= current_time - self.time_window:
                    self.requests.popleft()
                self.last_cleanup = current_time
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                return True
            
            return False

class RateLimiterWithCount:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.count = 0
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                self.count += 1
                return True
            
            return False
    
    def get_count(self) -> int:
        with self.lock:
            return self.count

class RateLimiterWithStatistics:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.stats = {
            'allowed': 0,
            'blocked': 0,
            'total': 0,
            'rate': 0.0
        }
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                self.stats['allowed'] += 1
                self.stats['total'] += 1
                self.stats['rate'] = self.stats['allowed'] / max(1, self.stats['total'])
                return True
            else:
                self.stats['blocked'] += 1
                self.stats['total'] += 1
                self.stats['rate'] = self.stats['allowed'] / max(1, self.stats['total'])
                return False
    
    def get_statistics(self) -> Dict[str, float]:
        with self.lock:
            return self.stats.copy()

class RateLimiterWithValidationEnhanced:
    def __init__(self, max_requests: int, time_window: int):
        if max_requests <= 0 or time_window <= 0:
            raise ValueError("max_requests and time_window must be positive")
        
        if max_requests > 1000000:
            raise ValueError("max_requests too large")
        
        if time_window > 86400:
            raise ValueError("time_window too large")
        
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
    
    def is_allowed(self, identifier: str = "default") -> bool:
        if not identifier or not isinstance(identifier, str):
            return False
        
        if len(identifier) > 1000:
            return False
        
        with self.lock:
            current_time = time.time()
            
            while self.requests and self.requests[0] <= current_time - self.time_window:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                return True
            
            return False

class RateLimiterWithOptimizationEnhanced:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.last_cleanup = time.time()
        self.cleanup_interval = time_window / 2
        self.stats = {
            'allowed': 0,
            'blocked': 0,
            'total': 0
        }
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            if current_time - self.last_cleanup > self.cleanup_interval:
                while self.requests and self.requests[0] <= current_time - self.time_window:
                    self.requests.popleft()
                self.last_cleanup = current_time
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                self.stats['allowed'] += 1
                self.stats['total'] += 1
                return True
            else:
                self.stats['blocked'] += 1
                self.stats['total'] += 1
                return False
    
    def get_stats(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()

class RateLimiterWithAdvancedOptimizationEnhanced:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.last_cleanup = time.time()
        self.cleanup_interval = time_window / 2
        self.stats = {
            'allowed': 0,
            'blocked': 0,
            'total': 0
        }
        self.memory_usage = 0
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            if current_time - self.last_cleanup > self.cleanup_interval:
                while self.requests and self.requests[0] <= current_time - self.time_window:
                    self.requests.popleft()
                self.last_cleanup = current_time
            
            if len(self.requests) < self.max_requests:
                self.requests.append(current_time)
                self.stats['allowed'] += 1
                self.stats['total'] += 1
                self.memory_usage += 8  # Approximate memory for timestamp
                return True
            else:
                self.stats['blocked'] += 1
                self.stats['total'] += 1
                return False
    
    def get_stats(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()
    
    def get_memory_usage(self) -> int:
        with self.lock:
            return self.memory_usage

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()
        self.lock = threading.Lock()
    
    def is_allowed(self, tokens: int = 1) -> bool:
        with self.lock:
            current_time = time.time()
            time_passed = current_time - self.last_refill
            
            self.tokens = min(self.capacity, self.tokens + time_passed * self.refill_rate)
            self.last_refill = current_time
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            
            return False

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)
        self.lock = threading.Lock()
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            cutoff_time = current_time - self.time_window
            
            self.requests[identifier] = [
                req_time for req_time in self.requests[identifier]
                if req_time > cutoff_time
            ]
            
            if len(self.requests[identifier]) < self.max_requests:
                self.requests[identifier].append(current_time)
                return True
            
            return False

class FixedWindowRateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.windows = defaultdict(lambda: {'count': 0, 'start_time': 0})
        self.lock = threading.Lock()
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            window_start = int(current_time // self.time_window) * self.time_window
            
            if self.windows[identifier]['start_time'] != window_start:
                self.windows[identifier] = {'count': 0, 'start_time': window_start}
            
            if self.windows[identifier]['count'] < self.max_requests:
                self.windows[identifier]['count'] += 1
                return True
            
            return False

class LeakyBucketRateLimiter:
    def __init__(self, capacity: int, leak_rate: float):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.bucket = 0
        self.last_leak = time.time()
        self.lock = threading.Lock()
    
    def is_allowed(self, requests: int = 1) -> bool:
        with self.lock:
            current_time = time.time()
            time_passed = current_time - self.last_leak
            
            self.bucket = max(0, self.bucket - time_passed * self.leak_rate)
            self.last_leak = current_time
            
            if self.bucket + requests <= self.capacity:
                self.bucket += requests
                return True
            
            return False

class RateLimiterWithAdvancedFeatures:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
        self.lock = threading.Lock()
        self.last_cleanup = time.time()
        self.cleanup_interval = time_window / 2
        self.stats = {
            'allowed': 0,
            'blocked': 0,
            'total': 0
        }
        self.memory_usage = 0
        self.peak_requests = 0
    
    def is_allowed(self, identifier: str = "default") -> bool:
        with self.lock:
            current_time = time.time()
            
            if current_time - self.last_cleanup > self.cleanup_interval:
                while self.requests and self.requests[0] <= current_time - self.time_window:
                    self.requests.popleft()
                self.last_cleanup = current_time
            
            current_requests = len(self.requests)
            self.peak_requests = max(self.peak_requests, current_requests)
            
            if current_requests < self.max_requests:
                self.requests.append(current_time)
                self.stats['allowed'] += 1
                self.stats['total'] += 1
                self.memory_usage += 8
                return True
            else:
                self.stats['blocked'] += 1
                self.stats['total'] += 1
                return False
    
    def get_stats(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()
    
    def get_memory_usage(self) -> int:
        with self.lock:
            return self.memory_usage
    
    def get_peak_requests(self) -> int:
        with self.lock:
            return self.peak_requests
    
    def get_current_requests(self) -> int:
        with self.lock:
            return len(self.requests)

max_requests = 10
time_window = 60

rl1 = RateLimiter(max_requests, time_window)
rl2 = RateLimiterOptimized(max_requests, time_window)
rl3 = RateLimiterWithValidation(max_requests, time_window)
rl4 = RateLimiterWithOptimization(max_requests, time_window)
rl5 = RateLimiterWithAdvancedOptimization(max_requests, time_window)
rl6 = RateLimiterWithCount(max_requests, time_window)
rl7 = RateLimiterWithStatistics(max_requests, time_window)
rl8 = RateLimiterWithValidationEnhanced(max_requests, time_window)
rl9 = RateLimiterWithOptimizationEnhanced(max_requests, time_window)
rl10 = RateLimiterWithAdvancedOptimizationEnhanced(max_requests, time_window)
rl11 = TokenBucketRateLimiter(max_requests, 1.0)
rl12 = SlidingWindowRateLimiter(max_requests, time_window)
rl13 = FixedWindowRateLimiter(max_requests, time_window)
rl14 = LeakyBucketRateLimiter(max_requests, 1.0)
rl15 = RateLimiterWithAdvancedFeatures(max_requests, time_window)

for i in range(15):
    allowed1 = rl1.is_allowed("user1")
    allowed2 = rl2.is_allowed("user1")
    allowed3 = rl3.is_allowed("user1")
    allowed4 = rl4.is_allowed("user1")
    allowed5 = rl5.is_allowed("user1")
    allowed6 = rl6.is_allowed("user1")
    allowed7 = rl7.is_allowed("user1")
    allowed8 = rl8.is_allowed("user1")
    allowed9 = rl9.is_allowed("user1")
    allowed10 = rl10.is_allowed("user1")
    allowed11 = rl11.is_allowed()
    allowed12 = rl12.is_allowed("user1")
    allowed13 = rl13.is_allowed("user1")
    allowed14 = rl14.is_allowed()
    allowed15 = rl15.is_allowed("user1")

stats2 = rl2.get_stats()
stats7 = rl7.get_statistics()
count6 = rl6.get_count()
stats9 = rl9.get_stats()
stats10 = rl10.get_stats()
memory10 = rl10.get_memory_usage()
stats15 = rl15.get_stats()
memory15 = rl15.get_memory_usage()
peak15 = rl15.get_peak_requests()
current15 = rl15.get_current_requests()

print(f"Max requests: {max_requests}")
print(f"Time window: {time_window}")
print(f"Allowed (basic): {allowed1}")
print(f"Allowed (optimized): {allowed2}")
print(f"Allowed (with validation): {allowed3}")
print(f"Allowed (with optimization): {allowed4}")
print(f"Allowed (advanced optimization): {allowed5}")
print(f"Allowed (with count): {allowed6}")
print(f"Allowed (with statistics): {allowed7}")
print(f"Allowed (validation enhanced): {allowed8}")
print(f"Allowed (optimization enhanced): {allowed9}")
print(f"Allowed (advanced optimization enhanced): {allowed10}")
print(f"Allowed (token bucket): {allowed11}")
print(f"Allowed (sliding window): {allowed12}")
print(f"Allowed (fixed window): {allowed13}")
print(f"Allowed (leaky bucket): {allowed14}")
print(f"Allowed (advanced features): {allowed15}")
print(f"Stats (optimized): {stats2}")
print(f"Stats (with statistics): {stats7}")
print(f"Count (with count): {count6}")
print(f"Stats (optimization enhanced): {stats9}")
print(f"Stats (advanced optimization enhanced): {stats10}")
print(f"Memory usage (advanced optimization enhanced): {memory10}")
print(f"Stats (advanced features): {stats15}")
print(f"Memory usage (advanced features): {memory15}")
print(f"Peak requests (advanced features): {peak15}")
print(f"Current requests (advanced features): {current15}")
