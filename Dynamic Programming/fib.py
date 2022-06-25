def fib(n):
    return _fib(n,{})

def _fib(n, memo):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
    return memo[n]