class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        
        zipped_lists = zip(position, speed)
        sorted_zipped = sorted(zipped_lists, reverse=True)
        sorted_position, sorted_speed = zip(*sorted_zipped)
        sorted_position = list(sorted_position)
        sorted_speed = list(sorted_speed)

        stack = []


        for i in range(n):
            v = sorted_speed[i]
            s_1 = sorted_position[i]

            s = target - s_1    

            t = s / v
            
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)


            