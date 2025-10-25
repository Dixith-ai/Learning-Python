import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
    
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

class MedianFinderOptimized:
    def __init__(self):
        self.small = []
        self.large = []
    
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

class MedianFinderWithValidation:
    def __init__(self):
        self.small = []
        self.large = []
    
    def addNum(self, num):
        if not isinstance(num, (int, float)):
            return
        
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if not self.small and not self.large:
            return None
        
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

class MedianFinderWithConstraints:
    def __init__(self, constraints):
        self.small = []
        self.large = []
        self.constraints = constraints
    
    def addNum(self, num):
        if not self.constraints(num):
            return
        
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if not self.small and not self.large:
            return None
        
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

class MedianFinderWithOptimization:
    def __init__(self):
        self.small = []
        self.large = []
    
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

class MedianFinderWithAdvancedOptimization:
    def __init__(self):
        self.small = []
        self.large = []
    
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

class MedianFinderWithCount:
    def __init__(self):
        self.small = []
        self.large = []
        self.count = 0
    
    def addNum(self, num):
        self.count += 1
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if self.count == 0:
            return None
        
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]
    
    def getCount(self):
        return self.count

class MedianFinderWithElements:
    def __init__(self):
        self.small = []
        self.large = []
        self.elements = []
    
    def addNum(self, num):
        self.elements.append(num)
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if not self.elements:
            return None
        
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]
    
    def getElements(self):
        return self.elements

class MedianFinderWithStatistics:
    def __init__(self):
        self.small = []
        self.large = []
        self.sum = 0
        self.min_val = float('inf')
        self.max_val = float('-inf')
    
    def addNum(self, num):
        self.sum += num
        self.min_val = min(self.min_val, num)
        self.max_val = max(self.max_val, num)
        
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]
    
    def getSum(self):
        return self.sum
    
    def getMin(self):
        return self.min_val
    
    def getMax(self):
        return self.max_val

nums = [1, 2, 3, 4, 5]

mf1 = MedianFinder()
mf2 = MedianFinderOptimized()
mf3 = MedianFinderWithValidation()
mf4 = MedianFinderWithOptimization()
mf5 = MedianFinderWithAdvancedOptimization()
mf6 = MedianFinderWithCount()
mf7 = MedianFinderWithElements()
mf8 = MedianFinderWithStatistics()

for num in nums:
    mf1.addNum(num)
    mf2.addNum(num)
    mf3.addNum(num)
    mf4.addNum(num)
    mf5.addNum(num)
    mf6.addNum(num)
    mf7.addNum(num)
    mf8.addNum(num)

median1 = mf1.findMedian()
median2 = mf2.findMedian()
median3 = mf3.findMedian()
median4 = mf4.findMedian()
median5 = mf5.findMedian()
median6 = mf6.findMedian()
count = mf6.getCount()
median7 = mf7.findMedian()
elements = mf7.getElements()
median8 = mf8.findMedian()
sum_val = mf8.getSum()
min_val = mf8.getMin()
max_val = mf8.getMax()

print(f"Numbers: {nums}")
print(f"Median (basic): {median1}")
print(f"Median (optimized): {median2}")
print(f"Median (with validation): {median3}")
print(f"Median (with optimization): {median4}")
print(f"Median (advanced optimization): {median5}")
print(f"Median (with count): {median6}, Count: {count}")
print(f"Median (with elements): {median7}, Elements: {elements}")
print(f"Median (with statistics): {median8}, Sum: {sum_val}, Min: {min_val}, Max: {max_val}")
