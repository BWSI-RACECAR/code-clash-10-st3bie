"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #10 - Song Analyzer (songanalyzer.py)


Author: Carter Berlind

Difficulty Level: 5/10

Prompt: Freddy is trying to write a song to impress his friends but needs help 
checking his lines. He decides to enlist you, a python programmer, to create a 
program to see if his lines are good. He tells you that he wants his lines to 
be judged off of whether they rhyme and how much alliteration is there.

Create a program in which the user can input a sentence and the program will 
report back how many words start with the same letters and what those letters 
are and how many words end in the same last three letters (If a word is less 
than three letters we do not consider its rhymes). 

Constraints: Words must be separated by a space. Only report if letters occur at the 
beginning of words multiple times. Don’t worry about commas and punctuation.

Test Cases:
Input: “carter is cool and not a fool”;                     Output: ”c=2,a=2, 2 rhyming words”
Input: “running jumping and swimming are really fun”;       Output: ”r=2, a=2, 3 rhyming words"
Input: “a ban on that book”;                                Output: ”b=2, 0 rhyming words”
Input: “good food for nice mice”;                           Output: ”f=2, 4 rhyming words”
Input: “howdy rowdy hikers hope you have a great time”;     Output: "h=4, 2 rhyming words”
"""

class Solution:
    def song_analyze(self, lyric):
        # type lyric: string
        # return: string 
        
        # TODO: Write code below to return a string with the solution to the prompt
        beginning = {}
        end = {}
        rhyme = {}
        
        words = lyric.split()
        
        for word in words:
            if (word[0] not in beginning):
                beginning[word[0]] = 1
            else:
                beginning[word[0]] += 1

            
            if (len(word) > 2):
                if (word[-3:] not in rhyme):
                    rhyme[word[-3:]] = 1
                else:
                    rhyme[word[-3:]] += 1
        
        output = ""
        rhyming = 0

        for key in beginning:
            if (beginning[key] > 1):
                output += str(key) + "=" + str(beginning[key]) + ", "

        for key in end:
            if (end[key] > 1):
                output += str(key) + "=" + str(end[key]) + ", "
        
        print(beginning)
        print(end)
        print(rhyme)
        for key in rhyme:
            if (rhyme[key] > 1):
                rhyming += rhyme[key]
        
        output += str(rhyming) + " rhyming words"

        return output

        

'''
            if (word[-1] not in end):
                end[word[-1]] = 1
            else:
                end[word[-1]] += 1
'''




def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.song_analyze(string1)
    print(ans)

if __name__ == "__main__":
    main()