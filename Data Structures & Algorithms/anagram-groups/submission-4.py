class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        """
        Loop through each str 
        sort the string
        If its in the hash map then add its index
        if not then create the entry

        str: list[indexes]
        """

        
        group_dict = {}
        for i, s in enumerate(strs):
            sorted_s_list = sorted(s)
            sorted_s = "".join(sorted_s_list)

            if sorted_s in group_dict:
                group_dict[sorted_s].append(i)
            else:
                group_dict[sorted_s] = [i]

        for sorted_s, index_list in group_dict.items():
            groups.append([strs[i] for i in index_list])

        return groups