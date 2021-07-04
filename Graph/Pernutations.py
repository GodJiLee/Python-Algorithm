# 1. generate pernutations using dfs
def permute(self, nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        # add result if leap node
        if len(elements) == 0:
            results.append(prev_elements[:]) # copy

        # call recursive function generating permutation
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop() # initialization

    dfs(nums)
    return results

# 2. using itertools module
import itertools
def permute(self, nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))
