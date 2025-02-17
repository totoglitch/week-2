#ex xp ninja
#ex 3:Instructions:Predict the output of the following code snippets:
#   >>> 3 <= 3 < 9  true
#    >>> 3 == 3 == 3 true
 #  >>> bool(0)  true
#    >>> bool(5 == "5") error
  # >>> bool(4 == 4) == bool("4" == "4") true
#    >>> bool(bool(None))  false
   #    x = (1 == True)  true
#   y = (1 == False)  false
#    a = True + 4 : error
 #    b = False + 10 :  error
 # print("x is", x) : error
   # print("y is", y) : error
  # print("a:", a) : error
  #  print("b":,b) : error
#ex 4 :Instructions:Use python to find out how many characters are in the following text, use a single line of code
 #(beyond the establishment of your my_text variable).
#my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua 
  # Ut enim ad minim veniam, quis nostrud exercitation ullamco  laboris nisi ut aliquip ex ea commodo consequat. 
#Duis aute irure dolor in reprehenderit in voluptate velit  esse cillum dolore eu fugiat nulla pariatur. 
#Excepteur sint occaecat cupidatat non proident,  sunt in cul
my_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit,  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua,"
" Ut enim ad minim veniam, quis nostrud exercitation ullamco  laboris nisi ut aliquip ex ea commodo consequat,"
"Duis aute irure dolor in reprehenderit in voluptate velit  esse cillum dolore eu fugiat nulla pariatur,"
"Excepteur sint occaecat cupidatat non proident,  sunt in cul"
len(my_text), print(len(my_text))
#ex 5 :Instructions:Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.
user_input=input("longest sentence without the letter A")
for "each new sentence" in user_input: print("congratulations")


