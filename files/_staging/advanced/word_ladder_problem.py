from collections import deque

def word_ladder_bfs(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return 0

def word_ladder_bfs_optimized(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return 0

def word_ladder_bfs_with_path(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0, []
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1, [begin_word])])
    visited = {begin_word}
    
    while queue:
        word, length, path = queue.popleft()
        
        if word == end_word:
            return length, path
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1, path + [new_word]))
    
    return 0, []

def word_ladder_bfs_with_validation(begin_word, end_word, word_list):
    if not begin_word or not end_word or not word_list:
        return 0
    
    if end_word not in word_list:
        return 0
    
    if begin_word == end_word:
        return 1
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return 0

def word_ladder_bfs_with_constraints(begin_word, end_word, word_list, constraints):
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited and constraints(new_word):
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return 0

def word_ladder_bfs_with_optimization(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return 0

def word_ladder_bfs_with_advanced_optimization(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return 0

def word_ladder_bfs_with_count(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0, 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    count = 0
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            count += 1
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))
    
    return length if count > 0 else 0, count

def word_ladder_bfs_with_all_paths(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0, []
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1, [begin_word])])
    visited = {begin_word}
    all_paths = []
    
    while queue:
        word, length, path = queue.popleft()
        
        if word == end_word:
            all_paths.append(path)
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1, path + [new_word]))
    
    return length if all_paths else 0, all_paths

begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

ladder1 = word_ladder_bfs(begin_word, end_word, word_list)
ladder2 = word_ladder_bfs_optimized(begin_word, end_word, word_list)
ladder3, path = word_ladder_bfs_with_path(begin_word, end_word, word_list)
ladder4 = word_ladder_bfs_with_validation(begin_word, end_word, word_list)
ladder5 = word_ladder_bfs_with_optimization(begin_word, end_word, word_list)
ladder6 = word_ladder_bfs_with_advanced_optimization(begin_word, end_word, word_list)
ladder7, count = word_ladder_bfs_with_count(begin_word, end_word, word_list)
ladder8, all_paths = word_ladder_bfs_with_all_paths(begin_word, end_word, word_list)

print(f"Begin word: {begin_word}")
print(f"End word: {end_word}")
print(f"Word list: {word_list}")
print(f"Word ladder (BFS): {ladder1}")
print(f"Word ladder (optimized): {ladder2}")
print(f"Word ladder (with path): {ladder3}, Path: {path}")
print(f"Word ladder (with validation): {ladder4}")
print(f"Word ladder (with optimization): {ladder5}")
print(f"Word ladder (advanced optimization): {ladder6}")
print(f"Word ladder (with count): {ladder7}, Count: {count}")
print(f"Word ladder (with all paths): {ladder8}, All paths: {all_paths}")
