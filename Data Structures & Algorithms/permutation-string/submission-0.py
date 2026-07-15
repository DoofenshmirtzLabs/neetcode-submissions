class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size=len(s1)
        counter_1={}
        current_window_counter={}
        start=0
        for i in s1:
            counter_1[i]=counter_1.get(i,0)+1
        for i in range(len(s2)):
         
            current_window_counter[s2[i]]=current_window_counter.get(s2[i],0)+1
        
            if i>=window_size-1:
                
                print(current_window_counter)
                if current_window_counter==counter_1:
                    return True
                current_window_counter[s2[start]]-=1
                if current_window_counter[s2[start]]==0:
                    del current_window_counter[s2[start]]
                start+=1
        return False
        