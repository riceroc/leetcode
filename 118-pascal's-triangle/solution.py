class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] # initialize the first row
        
        for i in range(numRows -1): # range over the length of input numRows -1 because of the above row
            temp = [0] + res[-1] + [0] # temporary array
            row = []                   # initialize empty row
            for j in range(len(res[-1]) + 1) : # for loop that builds next row
                row.append(temp[j] + temp[j+1]) # 2 pointers j/j+1 appending to the temp row
            res.append(row)                  # append the temp row to the result
        return res