class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        groups:defaultdict=defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            groups[sortedWord].append(word)
        

        for group in groups.values():
            final.append(group)

        return final