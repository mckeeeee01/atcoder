t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    inf = 10**18
    dp = [[inf]*3 for _ in range(n+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0
    
    for i in range(n):
        for j in range(3):
            cost = 0 if (int(s[i]) == (j % 2)) else 1
            dp[i+1][j] = min(dp[i+1][j],dp[i][j] + cost)
        
        for j in range(2):
            dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j])
        
    ans = dp[n][2]
    print(ans)
    
    
    


# T = int(input())

# for i in range(T):
#     n = int(input())
#     s = input()
    
#     ans = 0
#     state = 1
#     tmp_count_0 = 0 
#     tmp_count_1 = 0
#     for i in range(n):
#         if s[i] == "1":
#             if state == 0:
#                 ans += min(tmp_count_0,tmp_count_1)
#                 tmp_count_0 = 0
#                 tmp_count_1 = 0
#             state = 1
#             tmp_count_1 += 1
            
#         else: # s[i] == "0"
#             state = 0
#             tmp_count_0 += 1
    
    
#     print(ans)
            

                

    
    
    
    
    