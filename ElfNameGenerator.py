
# Elf Name Generator

# ----------------
# Constants
# ----------------
ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

ELF_ADJECTIVES = ["Jolly", "Sparkly", "Tiny", "Joyful", "Lively", "Gleeful", "Merry", "Cheery", "Frosty", "Fluffy", "Giggly", "Shiny", "Twinkly", "Spicy", "Cute", "Naughty", "Flying", "Fizzy", "Cheeky", "Jazzy", "Glowy", "Mirthful", "Glimmering", "Shining", "Bouncing", "Snuggly"]

ELF_NOUNS = ["Snowball", "Candycane", "Cocoa", "Tinsel", "Frost", "Wreath", "Gingerbread", "Bauble", "Sleigh", "Cookie", "Holly", "Mistletoe"]

# ----------------
# Subprograms
def generate_name(first_initial, birth_month):
    for i in range (0,len(ALPHABET)):
        if ALPHABET[i] == first_initial:
            adjective_index = i
    noun_index = birth_month -1 
    adjective = ELF_ADJECTIVES[adjective_index]
    noun = ELF_NOUNS[noun_index]
    name = adjective +" " + noun
    return name 
    #print (adjective_index)
    
# ----------------

# ----------------
# Main program
print("Welcome")
valid = False
while valid == False:
    first_initial = input("Enter first initial of your name: ")
    for j in range(0, len(ALPHABET)):
        if first_initial == ALPHABET[j]:
            valid = True 
valid = False
while valid == False:
    birth_month = int(input("Enter your birth month: "))
    if birth_month < 13 and birth_month > 0:
        valid = True 

elf_name = generate_name(first_initial,birth_month)
print("Your elf name is:", elf_name)

# ----------------