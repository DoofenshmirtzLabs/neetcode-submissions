class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #number of open brackets should be equal to number of closed brackets and sum==n*2

        def permutations(current_list,open_brackets,closed_brackets):
            total=open_brackets+closed_brackets
            print(current_list,n*2)
            if open_brackets==closed_brackets and total==n*2:
                if current_list not in memo:
                    memo.add(current_list)
                    res.append(current_list)
            
            if total>n*2:
                return

            permutations(current_list+'(',open_brackets+1,closed_brackets)
            #use ) only when there is an unmtached ( bracket
            if open_brackets!=closed_brackets:
                permutations(current_list+')',open_brackets,closed_brackets+1)
            current_list=current_list[:-1]

        memo=set()
        res=[]
        permutations('(',1,0)
        return res
            
