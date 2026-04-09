class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sent = set(sentence)
        return len(sent) == 26