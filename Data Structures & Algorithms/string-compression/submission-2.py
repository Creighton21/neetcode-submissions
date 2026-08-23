class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        s += chars[0]

        char_count = 0
        prev_char = chars[0]
        for c in chars:
            if c == prev_char:
                char_count += 1
                continue
            
            
            if char_count > 1:
                count_str = str(char_count)
                for ch in count_str:
                    s += ch

            s += c
            
            char_count = 1
            prev_char = c

        if char_count > 1:
            count_str = str(char_count)
            for ch in count_str:
                s += ch

    
        for key, val in enumerate(s):
            chars[key] = val

        return len(s)