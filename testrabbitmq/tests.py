# class Solution:
#     """
#     @param str: An array of char
#     @param offset: An integer
#     @return: nothing
#     """
#
#     def rotateString(self, s, offset):
#         # write your code here
#         s2 = s
#         slist = list(s)
#         for i in range(offset):
#             a = slist.pop()
#             slist.insert(0, a)
#         str2 = ''.join(str(i) for i in slist)
#         print(str2)
#         return str2
#
#
# if __name__ == "__main__":
#     a = Solution()
#     aa = a.rotateString('abcdefg', 3)
#     print(aa)

# def singleNumber(A):
#     # write your code here
#     A3 = A
#     the_one = 0
#
#     for i in A:
#         A2 = A[:]
#         A2.remove(i)
#         A4 = list(set(A2))
#         b = (len(A)-1)/2
#         if len(A2) - len(A4) == b:
#             the_one = i
#
#     return 111
#
# singleNumber([1,1,2,2,3,4,4])

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

def twoSum(numbers, target):
    # write your code here
    get_one = 0
    news = {}
    for key, val in enumerate(numbers):
        if val <= target:
            news[val] = key
    res = []
    for k, v in news.items():
        if news.__contains__(target - k):
            res.append(v)
    print(res)

numbers = [2,7,23,45,76]
target = 9
twoSum(numbers,target)