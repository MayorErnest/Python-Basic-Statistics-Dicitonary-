""" Project: Statistics Dictionary for DataScience
    By: Obumma Ernest Ndukwe
    Date: 03/01/2019
    Environment: Python Console
    version 1.0
""" 
import pandas as pd 
pd.set_option('max_colwidth',1000) # Set pandas dataframe display column width to 1000 to show full meaning without ellipses 
from difflib import get_close_matches 

Data = pd.read_excel('Database.xlsx') # Load excel file into pandas dataframe
Data = Data.set_index('Word') # Set dataframe index to column "Word" in other to fetch column "Meaning" using the index

def translate(w):
    """ This function checks if the input word exist in the dataframe, if it 
        does, it outputs its meaning, else it checks for close matches to the 
        input, if it finds, it ask users to verify if the close match word is the
        desired word, if true, it outputs its meaning, else it ouputs an error
        message.
    """
    if w in Data.index:
        return Data.loc[w] # Return meaning using indexing
    elif len(get_close_matches(w,Data.index)) > 0: # Check for close matches if any
        yn = input("Do you mean {}, y or n ? ".format(get_close_matches(w,Data.index)[0])) # Suggest close word to user if it exits.
        if yn == "y" or yn == "Y":
            return Data.loc[get_close_matches(w,Data.index)[0]] # Output meaning of the close word if users chose 'y'
        else:
            return "Sorry this word is not in this version of this dictionary."
    else: 
        return "This is not a basic statistical term."

word = input("Please input a statistical term: ").lower() # Ask for user input

output = translate(word) #load return value into variable

print(output) # Output return value