class Solution(object):
    def chalkReplacer(chalk, k):
        
        while k > 0:
            for c in chalk:
                ind = chalk.index(c)
                if c >= k:
                    k = 0
                    return ind
                else:
                    k -= c

print(Solution.chalkReplacer([16,29,70,14,81,16,21,70,66,45,65,37,72,58,58,98,63,6,61,1,18,37,97,90,100,75,59,73,50,100], 940635372))