
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = ""
        max_length = 0

        for char in s:
            if char in window:
                while char in window:
                    window = window[1:]

            window = window + char
            max_length = max(max_length, len(window))

        return max_length
