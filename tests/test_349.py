import pytest

# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         return list(set(nums1) & set(nums2))

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d1 = {}
        d2 = {}
        res = []
        for el in nums1:
            if el in d1:
                d1[el] += 1
            else:
                d1[el] = 1
        for el in nums2:
            if el in d2:
                d2[el] += 1
            else:
                d2[el] = 1
        for k in d1.keys():
            if k in d2:
               res.append(k)
        return res


@pytest.mark.parametrize("n1,n2, expected",
    [
        ([1,2,2,1], [2,2], [2]),
        ([4,9,5], [9,4,9,8,4], [9,4])
    ])
def test_intersection(n1, n2, expected):
    solution = Solution()
    assert solution.intersection(n1, n2).sort() == expected.sort()
