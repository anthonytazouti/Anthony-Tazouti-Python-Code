user_input = input("Enter in text.")
for letter in user_input:
   if letter.isalpha() and letter.isupper():
       print(letter)

for letter in range(len(user_input)):
    if user_input[letter].upper == "A" or user_input[letter].upper() == "E" or user_input[letter].upper() == "I" or user_input[letter].upper() == "O" or user_input[letter].upper() == "U" or user_input[letter].upper() == "Y":
        print(letter)



word = input("Enter in a word and I will print it backwards!")[::-1]
print(word)



palindrome = input("Enter in a word:")

if len(palindrome) != 5:
    print("Invalid entry, make it 5 letters.")
else:
   if palindrome[::-1] == palindrome:
        print("This is a palindrome!")
   else:
       print("You did not enter a palindrome.")




total_yard = 0.0
count = 0
yardgm1 = input(f"How many yards did QB pass for in game? {count+1} ")
while yardgm1 != "A":
    value = float(yardgm1)
    total_yard = total_yard + value
    count = count + 1
    yardgm1 = input(f"How many yards did QB pass for in game? {count+1} ")
    if count > 0:
        average = total_yard / count
    else:
        average = 0.0
print(f"The QB passed a total of {total_yard} and an average of {average:.2f} yards per game.")



LIMIT = 3

for row in range(1, LIMIT + 3):
    for col in range(1, LIMIT + 1):
        print(f"{row ** col:>4}", end="")
    print()
