class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        maxlt=0
        for i in range(len(gain)):
            alt+=gain[i]
            if alt>maxlt:
                maxlt=alt
        return maxlt