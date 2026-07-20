class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        s_2 = target

        time_map = defaultdict(list) # time it reaches, maps, list of indices

        for i in range(n):
            v = speed[i]
            s_1 = position[i]
            
            diff = s_2 - s_1
            t = diff / v
            
            lst = time_map[t]
            lst.append(i)
            time_map[t] = lst

        print(time_map)
        return len(time_map)
            

