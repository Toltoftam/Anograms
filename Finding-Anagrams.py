
# Finding-Anagrams/PK
# Finding-Anagrams/main.py# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

# Define users



user_1=input("User1: Please type in a word \n") # User1 should type in here  

user_2=input("User 2: Please type in a word \n")# User2 to type in here

def __init__():

    print("let us try again \n\n\n", user_1, user_2)


def anomsFunc():                         # to check if user input is an anogram
  
   s_user1 = sorted(user_1)                # sorts the word alphabetically
   
   s_user2 = sorted(user_2)                # sorts the word alphabetically
  
   while user_1 != int(user_1) or user_2 != int(user_2):
        
        while len(user_1) == len(user_2):
                if s_user1 == s_user2:
                    print("##############Anagram detected!################## \n")
                    
                    return True
                    # check if the sorted words match
                    try:
                        str(s_user1)
                        str(s_user2)
                        return True               #if the 1st iteration fails, check if user input is in string and then convert if not

                    except ValueError:
                        print("Invalid Value inputed, please try again \n")
                        # if there is an unknown value, alert user and return to the begining
                        return __init__

                    except TypeError:
                        print("You have not entered an input")      # if users did not enter any input
                        return __init__

                else:
                    
                    print("Words do not match, you have typed in an invalid value",)
                    return __init__


        else:
                print("Words do not match, please try again")
                return __init__

   else:
        return __init__

anomsFunc()
    

# Finding-Anagrams/PK 
#      -o�T�P�   �                /   Finding-Anagrams/main.pyPK      �   ,    