def nsum(n):
    sum = 0;
    for i in range(n+1):
        sum += i
    return sum

def nsum2(n):
    return sum([i for i in range(n+1)])

#recursion sum(n) = n + sum(n-1) 다시 함수를 호출하는 형태, base case: sum(0) = 0 지정을 안해주면 무한히 호출하게 된다.(베이스 컨디션이 중요하다.))
# sum(5)
# 5 + sum(4)
# 5 + 4 + sum(3)
# 5 + 4 + 3 + sum(2)
# 5 + 4 + 3 + 2 + sum(1)
# 5 + 4 + 3 + 2 + 1 + sum(0)
# 5 + 4 + 3 + 2 + 1 + (0 + sum(-1)) -> 무한히 호출
# 5 + 4 + 3 + 2 + 1 + (0 + sum(-2)) -> 무한히 호출 ...
# 5+ 4+ 3 + 2 + 1 + 0
# 5+ 4+ 3 + 2 + 1 
# 5+ 4+ 3 + 2
# 5+ 4+ 3
# 5+ 4
# 5
def nsum_recursive(n):
    if n == 0 :
        return 0
    else: 
        return n + sum(n-1)
    
# tail recursion
def sum_iter(n , total):
    if n == 0:
        return total
    else:
        return sum_iter(n-1, total + n)

# 지수 계산 b^n
def exponentiation(b,n):
    if n == 0:
        return 1
    
    else:
        return  b * exponentiation(b, n-1)
        
# tail recursion
def expt(b , counter , total):
    if counter == 0:
        return total
    else:
        return expt(b, counter-1, total * b)
    
    #Facst exponentiation
    
    def fast_expt(b, n):
        if n == 0:
            return 1
        # elif n % 2 == 0: # n이 짝수인 경우
        #     half_expt = fast_expt(b, n // 2)
        #     return half_expt * half_expt
        if even(n):
            return square(fast_expt(b, n / 2)) # n이 짝수인 경우 
        else:
            return b * fast_expt(b, n-1)
        
        
        # 피보나치
        def fibonacci(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
            
            
    