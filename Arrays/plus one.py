class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        print(f"This is s: {s}")
     
        # Join list items using join()
        res = int("".join(s))
        print(f"this is res: {res}")
        output = res + 1
        print(f"This is output{output}")
        result = [int(i) for i in str(output)]
        return result 
