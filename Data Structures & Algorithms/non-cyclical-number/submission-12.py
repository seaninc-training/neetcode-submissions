class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumSquares(n)

        while slow != fast and fast != 1:
            fast = self.sumSquares(self.sumSquares(fast))
            slow = self.sumSquares(slow)
        
        return True if fast == 1 else False

    def sumSquares(self, n: int) -> int:
        squares_sum = 0

        while n > 0:
            digit = n % 10
            squares_sum += (digit ** 2)
            n //= 10
        
        return squares_sum