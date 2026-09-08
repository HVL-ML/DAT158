def lcs_dynamic(x,y):
    rows=len(x) + 1
    columns = len(y) + 1

    #lager en tabell med nullere x og y aksen
    dp = [[0] * columns for _ in range(rows)]

    #start på 1 fordi rad og kolonne 0 representerer tom streng
    for i in range(1,rows):
        for j in range(1,columns):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],
                               dp[i][j-1]
                )
    return dp[len(x)][len(y)]

x = "babbababaaaaaabbbbbbbaaaaaaaaaaaaaaa"
y = "bbabbaaabaaaaaaaaaaaaaaaaaaaaaaaaaaa"

result = lcs_dynamic(x, y)
print("Lengda på LCS:", result)