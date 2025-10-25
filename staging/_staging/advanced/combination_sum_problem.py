def combination_sum_backtracking(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_optimized(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_validation(candidates, target):
    if not candidates or target <= 0:
        return []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_constraints(candidates, target, constraints):
    def backtrack(start, current, remaining):
        if remaining == 0:
            if constraints(current):
                result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_optimization(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_advanced_optimization(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_count(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result, len(result)

def combination_sum_backtracking_with_permutations(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_repetition(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_duplicates(candidates, target):
    candidates.sort()
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_validation_enhanced(candidates, target):
    if not candidates or target <= 0:
        return []
    
    if target == 0:
        return [[]]
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_optimization_enhanced(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_advanced_optimization_enhanced(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    return result

def combination_sum_backtracking_with_statistics(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    
    return result, {
        'count': len(result),
        'target': target,
        'candidates': len(candidates)
    }

def combination_sum_backtracking_with_advanced_features(candidates, target):
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    
    result = []
    backtrack(0, [], target)
    
    return result, {
        'count': len(result),
        'target': target,
        'candidates': len(candidates),
        'min_length': min(len(combo) for combo in result) if result else 0,
        'max_length': max(len(combo) for combo in result) if result else 0
    }

candidates = [2, 3, 6, 7]
target = 7

combinations1 = combination_sum_backtracking(candidates, target)
combinations2 = combination_sum_backtracking_optimized(candidates, target)
combinations3 = combination_sum_backtracking_with_validation(candidates, target)
combinations4 = combination_sum_backtracking_with_optimization(candidates, target)
combinations5 = combination_sum_backtracking_with_advanced_optimization(candidates, target)
combinations6, count = combination_sum_backtracking_with_count(candidates, target)
combinations7 = combination_sum_backtracking_with_permutations(candidates, target)
combinations8 = combination_sum_backtracking_with_repetition(candidates, target)
combinations9 = combination_sum_backtracking_with_duplicates(candidates, target)
combinations10 = combination_sum_backtracking_with_validation_enhanced(candidates, target)
combinations11 = combination_sum_backtracking_with_optimization_enhanced(candidates, target)
combinations12 = combination_sum_backtracking_with_advanced_optimization_enhanced(candidates, target)
combinations13, stats = combination_sum_backtracking_with_statistics(candidates, target)
combinations14, features = combination_sum_backtracking_with_advanced_features(candidates, target)

print(f"Candidates: {candidates}")
print(f"Target: {target}")
print(f"Combinations (backtracking): {combinations1}")
print(f"Combinations (optimized): {combinations2}")
print(f"Combinations (with validation): {combinations3}")
print(f"Combinations (with optimization): {combinations4}")
print(f"Combinations (advanced optimization): {combinations5}")
print(f"Combinations (with count): {combinations6}, Count: {count}")
print(f"Combinations (with permutations): {combinations7}")
print(f"Combinations (with repetition): {combinations8}")
print(f"Combinations (with duplicates): {combinations9}")
print(f"Combinations (validation enhanced): {combinations10}")
print(f"Combinations (optimization enhanced): {combinations11}")
print(f"Combinations (advanced optimization enhanced): {combinations12}")
print(f"Combinations (with statistics): {combinations13}, Statistics: {stats}")
print(f"Combinations (with advanced features): {combinations14}, Features: {features}")
