class Solution(object):
    def RotateArray(self, array):
        sCol = 0
        eCol = len(array[0]) - 1
        filler = 0
        while sCol <= eCol:
            for x in range(sCol, eCol):
                temp = array[sCol][x]
                array[sCol][x] = array[x][eCol]
                array[x][eCol] = array[eCol][eCol - x + filler]
                array[eCol][eCol - x + filler] = array[eCol - x + filler][sCol]
                array[eCol - x + filler][sCol] = temp
            sCol += 1
            eCol -= 1
            filler += 1
        return array


if __name__ == "__main__":
    answer = Solution()
    print(answer.RotateArray([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
    # print(answer.RotateArray([[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]))