
#create a mad lib that asks the user for each word to put in.

####
# I scoured my closet for the perfect ____________ to wear. Dressing for the ________ place
#  Article of clothing Superlative
# around isn’t easy. Sweating _________ during the interview is a sure sign of weakness. I must
#  Plural noun
# remember to play up my strengths: _______, menacing stares, and _______ collecting.
# Sport Noun
# It has always been my dream to work with the Angel of Death, or _________ Devil. 
#  Personal title


# assign each input to a variable 
articleocloth = input("Enter an article of clothing: ")
articleocloth2 = input("Enter another article of clothing: ")
noun = input("Enter a plural noun: ")
Sportnoun = input("Enter a sport noun: ")
Sportnoun2 = input("Enter another sport noun: ")
Title = input("Enter a Title: ")

print(f''' I scoured my closet for the perfect{articleocloth} to wear. Dressing for the {articleocloth2}
 place around isn’t easy. Sweating {noun} during the interview is a sure sign of weakness. I must
 remember to play up my strengths: {Sportnoun} , menacing stares, and {Sportnoun2} collecting.
 It has always been my dream to work with the Angel of Death, or {Title} Devil. 
''')
