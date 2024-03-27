
def count_letters(word, letter):
    count = 0 #go ahead and just put it here
    for char in word: 
        if char == letter: #you can ignore this line and just do "letter in word"  
            count +=1
            
    return count

def main():
    print("Number of o's in frivolous is",
          count_letters("frivolous", "o")) #this IS where you specify word and letter
    print("notes.py", __name__) #this becomes main when we run the function
    if  __name__ == "__main__": # this checks if you are running the first file or the copy file
        main() # and only prints the output for the file you want

#import THIS file into wherever you need it, this file is notes.py
# notes.count_letters("frivolous", "o"))

'''
how it would look imported ^^
so both THIS data, and the newly coded data would print
'''

def reverse_grades(final_grades):
    resversed_dict = {}
    for name in final_grades:  #checks if the grade already exists too
        grade = final_grades[name]
        if grade not in reversed_dict: #checks if the grade already exists too
            reversed_dict[grade] = []
        reversed_dict[grade].append(name) #huh ok make a new list of "grades" and add a NAME to it
    return reversed_dict #tell me who got a 90, and and then add a name to THAT

