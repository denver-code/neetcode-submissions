class Solution:

    def encode(self, strs: List[str]) -> str:
        lenghts = ""
        es = "".join(strs)

        for i, s in enumerate(strs):
           lenghts += f"{len(s)}{'-' if i != len(strs)-1 else '..'}"


        return lenghts+es

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == "":
            return [""]
        payloads = s.split("..", 1)
        lenghts = payloads[0].split("-")
        payload = "".join(payloads[1:])
        result = []
        pointer = 0
        for l in lenghts:
             l = int(l)
             word = payload[pointer:pointer+l]
             result.append(word)
             pointer += l

        return result