import hashlib
import random
import string
from collections import defaultdict

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
    
    def generate_code(self, url):
        hash_object = hashlib.md5(url.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig[:self.code_length]
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code(url)
        while code in self.code_to_url:
            code = self.generate_code(url + str(random.randint(0, 9999)))
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerOptimized:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithValidation:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def is_valid_url(self, url):
        return url.startswith(('http://', 'https://'))
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if not self.is_valid_url(url):
            return None
        
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        if not short_url.startswith(self.base_url):
            return None
        
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithConstraints:
    def __init__(self, constraints):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
        self.constraints = constraints
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if not self.constraints(url):
            return None
        
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithOptimization:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithAdvancedOptimization:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithCount:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
        self.count = 0
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        self.count += 1
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)
    
    def get_count(self):
        return self.count

class URLShortenerWithStatistics:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
        self.stats = {
            'total_urls': 0,
            'unique_urls': 0,
            'duplicate_urls': 0
        }
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        self.stats['total_urls'] += 1
        
        if url in self.url_to_code:
            self.stats['duplicate_urls'] += 1
            return self.base_url + self.url_to_code[url]
        
        self.stats['unique_urls'] += 1
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)
    
    def get_statistics(self):
        return self.stats

class URLShortenerWithValidationEnhanced:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def is_valid_url(self, url):
        return url.startswith(('http://', 'https://')) and len(url) > 10
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if not self.is_valid_url(url):
            return None
        
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        if not short_url.startswith(self.base_url):
            return None
        
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithOptimizationEnhanced:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithAdvancedOptimizationEnhanced:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.code_to_url.get(code, None)

class URLShortenerWithAdvancedFeatures:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://short.ly/"
        self.code_length = 6
        self.chars = string.ascii_letters + string.digits
        self.click_count = defaultdict(int)
        self.creation_time = {}
    
    def generate_code(self):
        return ''.join(random.choices(self.chars, k=self.code_length))
    
    def shorten_url(self, url):
        if url in self.url_to_code:
            return self.base_url + self.url_to_code[url]
        
        code = self.generate_code()
        while code in self.code_to_url:
            code = self.generate_code()
        
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        self.creation_time[code] = __import__('time').time()
        
        return self.base_url + code
    
    def expand_url(self, short_url):
        code = short_url.replace(self.base_url, "")
        if code in self.code_to_url:
            self.click_count[code] += 1
            return self.code_to_url[code]
        return None
    
    def get_click_count(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.click_count.get(code, 0)
    
    def get_creation_time(self, short_url):
        code = short_url.replace(self.base_url, "")
        return self.creation_time.get(code, None)

url = "https://www.example.com/very/long/url/that/needs/to/be/shortened"

shortener1 = URLShortener()
shortener2 = URLShortenerOptimized()
shortener3 = URLShortenerWithValidation()
shortener4 = URLShortenerWithOptimization()
shortener5 = URLShortenerWithAdvancedOptimization()
shortener6 = URLShortenerWithCount()
shortener7 = URLShortenerWithStatistics()
shortener8 = URLShortenerWithValidationEnhanced()
shortener9 = URLShortenerWithOptimizationEnhanced()
shortener10 = URLShortenerWithAdvancedOptimizationEnhanced()
shortener11 = URLShortenerWithAdvancedFeatures()

short1 = shortener1.shorten_url(url)
expanded1 = shortener1.expand_url(short1)
short2 = shortener2.shorten_url(url)
expanded2 = shortener2.expand_url(short2)
short3 = shortener3.shorten_url(url)
expanded3 = shortener3.expand_url(short3)
short4 = shortener4.shorten_url(url)
expanded4 = shortener4.expand_url(short4)
short5 = shortener5.shorten_url(url)
expanded5 = shortener5.expand_url(short5)
short6 = shortener6.shorten_url(url)
expanded6 = shortener6.expand_url(short6)
count = shortener6.get_count()
short7 = shortener7.shorten_url(url)
expanded7 = shortener7.expand_url(short7)
stats = shortener7.get_statistics()
short8 = shortener8.shorten_url(url)
expanded8 = shortener8.expand_url(short8)
short9 = shortener9.shorten_url(url)
expanded9 = shortener9.expand_url(short9)
short10 = shortener10.shorten_url(url)
expanded10 = shortener10.expand_url(short10)
short11 = shortener11.shorten_url(url)
expanded11 = shortener11.expand_url(short11)
click_count = shortener11.get_click_count(short11)
creation_time = shortener11.get_creation_time(short11)

print(f"Original URL: {url}")
print(f"Shortened (basic): {short1}")
print(f"Expanded (basic): {expanded1}")
print(f"Shortened (optimized): {short2}")
print(f"Expanded (optimized): {expanded2}")
print(f"Shortened (with validation): {short3}")
print(f"Expanded (with validation): {expanded3}")
print(f"Shortened (with optimization): {short4}")
print(f"Expanded (with optimization): {expanded4}")
print(f"Shortened (advanced optimization): {short5}")
print(f"Expanded (advanced optimization): {expanded5}")
print(f"Shortened (with count): {short6}")
print(f"Expanded (with count): {expanded6}, Count: {count}")
print(f"Shortened (with statistics): {short7}")
print(f"Expanded (with statistics): {expanded7}, Statistics: {stats}")
print(f"Shortened (validation enhanced): {short8}")
print(f"Expanded (validation enhanced): {expanded8}")
print(f"Shortened (optimization enhanced): {short9}")
print(f"Expanded (optimization enhanced): {expanded9}")
print(f"Shortened (advanced optimization enhanced): {short10}")
print(f"Expanded (advanced optimization enhanced): {expanded10}")
print(f"Shortened (with advanced features): {short11}")
print(f"Expanded (with advanced features): {expanded11}")
print(f"Click count: {click_count}")
print(f"Creation time: {creation_time}")
