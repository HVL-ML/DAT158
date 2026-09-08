def lcs_recursive(x,y,i,j):
    #strenger er tom(base case)
    if i == 0 or j == 0:
        return 0
    #tegnene er like
    if x[i-1] == y[j-1]:
        return 1 + lcs_recursive(x,y,i-1,j-1)

    #tegnene er ulike
    return max(
        lcs_recursive(x,y,i-1,j),
        lcs_recursive(x,y,i,j-1)
    )
x = "babbababaaaaaabbbbbbbaaaaaaaaaaaaaaa"
y = "bbabbaaabaaaaaaaaaaaaaaaaaaaaaaaaaaa"

result = lcs_recursive(x,y,len(x),len(y))
print("lengden på lcs er: ", result)
