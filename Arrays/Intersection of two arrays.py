class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l,r = 0,0
        output= []
        #sort the arrays 
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        while l < len(nums1) and r < len(nums2):
            if nums1[l]< nums2[r]:
                l+=1
            elif nums1[l]>nums2[r]:
                r+=1
            else:
                output.append(nums1[l])
                l+=1
                r+=1
        return output
