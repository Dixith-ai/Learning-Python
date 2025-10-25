import time
import threading
from collections import defaultdict, OrderedDict
from typing import Any, Optional, List, Dict, Set

class KeyValueStore:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)

class KeyValueStoreOptimized:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.stats = {
            'hits': 0,
            'misses': 0,
            'sets': 0,
            'deletes': 0
        }
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            self.stats['sets'] += 1
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                self.stats['misses'] += 1
                return None
            
            if key in self.data:
                self.stats['hits'] += 1
                return self.data[key]
            else:
                self.stats['misses'] += 1
                return None
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                self.stats['deletes'] += 1
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_stats(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()

class KeyValueStoreWithValidation:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.max_key_length = 1000
        self.max_value_size = 1024 * 1024  # 1MB
    
    def _validate_key(self, key: str) -> bool:
        return isinstance(key, str) and len(key) <= self.max_key_length
    
    def _validate_value(self, value: Any) -> bool:
        if isinstance(value, str):
            return len(value) <= self.max_value_size
        return True
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        if not self._validate_key(key) or not self._validate_value(value):
            return False
        
        with self.lock:
            self.data[key] = value
            if ttl and ttl > 0:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        if not self._validate_key(key):
            return None
        
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        if not self._validate_key(key):
            return False
        
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                return True
            return False
    
    def exists(self, key: str) -> bool:
        if not self._validate_key(key):
            return False
        
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        if not self._validate_key(key):
            return -2
        
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)

class KeyValueStoreWithConstraints:
    def __init__(self, constraints):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.constraints = constraints
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        if not self.constraints(key, value):
            return False
        
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)

class KeyValueStoreWithOptimization:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.access_count = defaultdict(int)
        self.last_access = {}
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            
            if key in self.data:
                self.access_count[key] += 1
                self.last_access[key] = time.time()
                return self.data[key]
            return None
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                self.access_count.pop(key, None)
                self.last_access.pop(key, None)
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_access_count(self, key: str) -> int:
        with self.lock:
            return self.access_count.get(key, 0)
    
    def get_last_access(self, key: str) -> Optional[float]:
        with self.lock:
            return self.last_access.get(key)

class KeyValueStoreWithAdvancedOptimization:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.access_count = defaultdict(int)
        self.last_access = {}
        self.hot_keys = set()
        self.cold_keys = set()
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            
            if key in self.data:
                self.access_count[key] += 1
                self.last_access[key] = time.time()
                
                if self.access_count[key] > 10:
                    self.hot_keys.add(key)
                    self.cold_keys.discard(key)
                elif self.access_count[key] < 5:
                    self.cold_keys.add(key)
                    self.hot_keys.discard(key)
                
                return self.data[key]
            return None
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                self.access_count.pop(key, None)
                self.last_access.pop(key, None)
                self.hot_keys.discard(key)
                self.cold_keys.discard(key)
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_hot_keys(self) -> Set[str]:
        with self.lock:
            return self.hot_keys.copy()
    
    def get_cold_keys(self) -> Set[str]:
        with self.lock:
            return self.cold_keys.copy()

class KeyValueStoreWithCount:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.count = 0
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            if key not in self.data:
                self.count += 1
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                self.count -= 1
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_count(self) -> int:
        with self.lock:
            return self.count

class KeyValueStoreWithStatistics:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.stats = {
            'hits': 0,
            'misses': 0,
            'sets': 0,
            'deletes': 0,
            'expired': 0
        }
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            self.stats['sets'] += 1
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                self.stats['expired'] += 1
                self.stats['misses'] += 1
                return None
            
            if key in self.data:
                self.stats['hits'] += 1
                return self.data[key]
            else:
                self.stats['misses'] += 1
                return None
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                self.stats['deletes'] += 1
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_statistics(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()

class KeyValueStoreWithValidationEnhanced:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.max_key_length = 1000
        self.max_value_size = 1024 * 1024  # 1MB
        self.max_ttl = 86400 * 365  # 1 year
    
    def _validate_key(self, key: str) -> bool:
        return isinstance(key, str) and len(key) <= self.max_key_length and key.strip()
    
    def _validate_value(self, value: Any) -> bool:
        if isinstance(value, str):
            return len(value) <= self.max_value_size
        return True
    
    def _validate_ttl(self, ttl: Optional[int]) -> bool:
        return ttl is None or (isinstance(ttl, int) and 0 < ttl <= self.max_ttl)
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        if not self._validate_key(key) or not self._validate_value(value) or not self._validate_ttl(ttl):
            return False
        
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            return True
    
    def get(self, key: str) -> Optional[Any]:
        if not self._validate_key(key):
            return None
        
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return None
            return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        if not self._validate_key(key):
            return False
        
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                return True
            return False
    
    def exists(self, key: str) -> bool:
        if not self._validate_key(key):
            return False
        
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        if not self._validate_key(key):
            return -2
        
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)

class KeyValueStoreWithOptimizationEnhanced:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.access_count = defaultdict(int)
        self.last_access = {}
        self.hot_keys = set()
        self.cold_keys = set()
        self.stats = {
            'hits': 0,
            'misses': 0,
            'sets': 0,
            'deletes': 0
        }
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            self.data[key] = value
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            self.stats['sets'] += 1
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                self.stats['misses'] += 1
                return None
            
            if key in self.data:
                self.access_count[key] += 1
                self.last_access[key] = time.time()
                self.stats['hits'] += 1
                
                if self.access_count[key] > 10:
                    self.hot_keys.add(key)
                    self.cold_keys.discard(key)
                elif self.access_count[key] < 5:
                    self.cold_keys.add(key)
                    self.hot_keys.discard(key)
                
                return self.data[key]
            else:
                self.stats['misses'] += 1
                return None
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                del self.data[key]
                self.expiry.pop(key, None)
                self.access_count.pop(key, None)
                self.last_access.pop(key, None)
                self.hot_keys.discard(key)
                self.cold_keys.discard(key)
                self.stats['deletes'] += 1
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_hot_keys(self) -> Set[str]:
        with self.lock:
            return self.hot_keys.copy()
    
    def get_cold_keys(self) -> Set[str]:
        with self.lock:
            return self.cold_keys.copy()
    
    def get_statistics(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()

class KeyValueStoreWithAdvancedOptimizationEnhanced:
    def __init__(self):
        self.data = {}
        self.expiry = {}
        self.lock = threading.RLock()
        self.access_count = defaultdict(int)
        self.last_access = {}
        self.hot_keys = set()
        self.cold_keys = set()
        self.stats = {
            'hits': 0,
            'misses': 0,
            'sets': 0,
            'deletes': 0
        }
        self.memory_usage = 0
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        with self.lock:
            if key in self.data:
                self.memory_usage -= len(str(self.data[key]))
            else:
                self.memory_usage += len(str(key))
            
            self.data[key] = value
            self.memory_usage += len(str(value))
            
            if ttl:
                self.expiry[key] = time.time() + ttl
            else:
                self.expiry.pop(key, None)
            self.stats['sets'] += 1
            return True
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                self.stats['misses'] += 1
                return None
            
            if key in self.data:
                self.access_count[key] += 1
                self.last_access[key] = time.time()
                self.stats['hits'] += 1
                
                if self.access_count[key] > 10:
                    self.hot_keys.add(key)
                    self.cold_keys.discard(key)
                elif self.access_count[key] < 5:
                    self.cold_keys.add(key)
                    self.hot_keys.discard(key)
                
                return self.data[key]
            else:
                self.stats['misses'] += 1
                return None
    
    def delete(self, key: str) -> bool:
        with self.lock:
            if key in self.data:
                self.memory_usage -= len(str(key)) + len(str(self.data[key]))
                del self.data[key]
                self.expiry.pop(key, None)
                self.access_count.pop(key, None)
                self.last_access.pop(key, None)
                self.hot_keys.discard(key)
                self.cold_keys.discard(key)
                self.stats['deletes'] += 1
                return True
            return False
    
    def exists(self, key: str) -> bool:
        with self.lock:
            if key in self.expiry and time.time() > self.expiry[key]:
                self.delete(key)
                return False
            return key in self.data
    
    def keys(self, pattern: str = "*") -> List[str]:
        with self.lock:
            if pattern == "*":
                return list(self.data.keys())
            return [k for k in self.data.keys() if pattern in k]
    
    def ttl(self, key: str) -> int:
        with self.lock:
            if key not in self.data:
                return -2
            if key not in self.expiry:
                return -1
            remaining = int(self.expiry[key] - time.time())
            return max(0, remaining)
    
    def get_hot_keys(self) -> Set[str]:
        with self.lock:
            return self.hot_keys.copy()
    
    def get_cold_keys(self) -> Set[str]:
        with self.lock:
            return self.cold_keys.copy()
    
    def get_statistics(self) -> Dict[str, int]:
        with self.lock:
            return self.stats.copy()
    
    def get_memory_usage(self) -> int:
        with self.lock:
            return self.memory_usage

kv1 = KeyValueStore()
kv2 = KeyValueStoreOptimized()
kv3 = KeyValueStoreWithValidation()
kv4 = KeyValueStoreWithOptimization()
kv5 = KeyValueStoreWithAdvancedOptimization()
kv6 = KeyValueStoreWithCount()
kv7 = KeyValueStoreWithStatistics()
kv8 = KeyValueStoreWithValidationEnhanced()
kv9 = KeyValueStoreWithOptimizationEnhanced()
kv10 = KeyValueStoreWithAdvancedOptimizationEnhanced()

kv1.set("key1", "value1", 60)
kv2.set("key1", "value1", 60)
kv3.set("key1", "value1", 60)
kv4.set("key1", "value1", 60)
kv5.set("key1", "value1", 60)
kv6.set("key1", "value1", 60)
kv7.set("key1", "value1", 60)
kv8.set("key1", "value1", 60)
kv9.set("key1", "value1", 60)
kv10.set("key1", "value1", 60)

value1 = kv1.get("key1")
value2 = kv2.get("key1")
value3 = kv3.get("key1")
value4 = kv4.get("key1")
value5 = kv5.get("key1")
value6 = kv6.get("key1")
value7 = kv7.get("key1")
value8 = kv8.get("key1")
value9 = kv9.get("key1")
value10 = kv10.get("key1")

stats2 = kv2.get_stats()
stats7 = kv7.get_statistics()
count6 = kv6.get_count()
hot_keys5 = kv5.get_hot_keys()
cold_keys5 = kv5.get_cold_keys()
hot_keys9 = kv9.get_hot_keys()
cold_keys9 = kv9.get_cold_keys()
stats9 = kv9.get_statistics()
stats10 = kv10.get_statistics()
memory10 = kv10.get_memory_usage()

print(f"Key: key1")
print(f"Value (basic): {value1}")
print(f"Value (optimized): {value2}")
print(f"Value (with validation): {value3}")
print(f"Value (with optimization): {value4}")
print(f"Value (advanced optimization): {value5}")
print(f"Value (with count): {value6}")
print(f"Value (with statistics): {value7}")
print(f"Value (validation enhanced): {value8}")
print(f"Value (optimization enhanced): {value9}")
print(f"Value (advanced optimization enhanced): {value10}")
print(f"Stats (optimized): {stats2}")
print(f"Stats (with statistics): {stats7}")
print(f"Count (with count): {count6}")
print(f"Hot keys (advanced optimization): {hot_keys5}")
print(f"Cold keys (advanced optimization): {cold_keys5}")
print(f"Hot keys (optimization enhanced): {hot_keys9}")
print(f"Cold keys (optimization enhanced): {cold_keys9}")
print(f"Stats (optimization enhanced): {stats9}")
print(f"Stats (advanced optimization enhanced): {stats10}")
print(f"Memory usage (advanced optimization enhanced): {memory10}")
