class Solution:
    def canCompleteCircuit_on2(self, gas: List[int], cost: List[int]) -> int:
        # 18:00 - 18:09
        if sum(gas) < sum(cost):
            return -1
        
        def helper(depth, cur_pos, tot_gas):
            if depth == len(gas):
                return True
            tot_gas += gas[cur_pos] - cost[cur_pos]
            if tot_gas >= 0:
                return helper(depth + 1, (cur_pos + 1) % len(gas), tot_gas)
            return False
        
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if helper(0, i, 0):
                    return i
        return -1

    def canCompleteCircuit_on(self, gas: List[int], cost: List[int]) -> int:
        # 18:10 - 18:13
        if sum(gas) < sum(cost):
            return -1
        
        cur_gas = 0
        start = 0
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
        return start
        
            