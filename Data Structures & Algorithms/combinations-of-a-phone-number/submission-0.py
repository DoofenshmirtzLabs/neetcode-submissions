class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letters={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def combinations(start,current_list):

            if len(current_list)==n:
                res.append(current_list)
                return


            

            for char in letters[digits[start]]:
                combinations(start+1,current_list+char)




        n=len(digits)
        res=[]
        if digits:
            combinations(0,'')

        return res