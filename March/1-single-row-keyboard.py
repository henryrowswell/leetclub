'''
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3656/


Single-Row Keyboard

There is a special keyboard with all keys in a single row.
Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.
You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

 

Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 
Example 2:

Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73
 

Constraints:

keyboard.length == 26
keyboard contains each English lowercase letter exactly once in some order.
1 <= word.length <= 10^4
word[i] is an English lowercase letter.

'''

'''
Time complexity:
O(n) where n is number of letters in word. Linear because we loop through every letter of the word. Worst case, we search through the entire keyboard
to find each letter, however the keyboard is at most length 26 so it's 26n, rather than n^2. (Worst case scenario is every other letter
at opposite ends of the keyboard e.g azazaz)

Space complexity: O(1)

Improvements:
-   pre-process keyboard: iterate through the keyboard once (O(1) since keyboard is constant length of 26), store a dictionary of letter:index key value pairs,
    that way you can look them up in constant time. This is still O(n) since you still have to loop through the word, it only reduces the lookup of each letter from
    O(26) (constant) to O(1) (still constant) so it doesn't really change anything.
-   memoize: when you find the index of a letter on the keyboard, store it. When looking up letters, check your memoize dictionary first. Same as above, but building
    the dictionary as you go instead of preprocessing (e.g if keyboard was too long to preprocess). Still, doesn't really change runtime unless keyboard lookup was
    somehow the limiting factor.
'''

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # currentIndex, sum
        # for letter in word, find index of that letter, add diff between currentIndex and letterIndex to sum, update currentIndex, and continue looping
        
        currIndex = 0
        currSum = 0
        for letter in word:
            letterIndex = keyboard.index(letter)
            currSum += abs(letterIndex - currIndex)
            currIndex = letterIndex
        
        return currSum