class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += f"{len(i)}#{i}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        chr_count_str = ""
        chr_count = 0
        chr_string = ""
        isCount = True
        for i in s:
            if i == "#" and isCount:
                chr_count = int(chr_count_str)
                if chr_count == 0:
                    result.append("")
                else:
                    isCount = False
                continue
            if isCount:
                chr_count_str += i
                continue
            
            if chr_count > 0:
                chr_string += i
                chr_count -= 1
            
            if chr_count == 0:
                result.append(chr_string)
                isCount = True
                chr_string = ""
                chr_count_str = ""

        return result