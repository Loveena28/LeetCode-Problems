class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resultStr = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                resultStr.append("FizzBuzz")
            elif i%3 == 0:
                resultStr.append("Fizz")
            elif i%5 == 0:
                resultStr.append("Buzz")
            else:
                resultStr.append(str(i))
        return resultStr