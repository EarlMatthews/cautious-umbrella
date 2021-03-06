def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo): 
    if amount in memo:  
        return memo[amount]
    
    if amount < 0:
        return False
    
    if amount == 0:
        return True
     
    for num in numbers:
        memo[amount] = _sum_possible(amount - num, numbers, memo)
        if  memo[amount] == True:
            return True
      
    return False