from pychord import Chord

#Calls pychord function and returns all chords in a chords object
def get_progression(root, progression):
    progList, chords = [], []

    #empty progression or root
    if not progression:
        print("Error: empty progression")
        return chords
    
    if not root:
        print("Error: empty root")
        return chords

    #conversion
    progList = romanToInt(progression)
    checkedRoot = checkRoot(root)

    #finding chords
    try:
        for x in progList:
            chord = Chord.from_note_index(x, "", checkedRoot, diatonic=True)
            chords.append(chord)
    except:
        print("Error: chord not found")
    
    return chords

#Checks for implicit major roots and converts them to be explicit
def checkRoot(root):
    
    major = {
        "A":"Amaj", "B": "Bmaj", "C": "Cmaj", "D": "Dmaj", "E": "Emaj", "F": "Fmaj"
    }

    if root in major:
        checkedRoot = major[root]
    else:
        checkedRoot = root
    
    return checkedRoot

#Converting Roman Numerals into Integars
def romanToInt(progression):
    progList = []

    numbers = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7
    }

    if isinstance(progression, str):
        temp = progression.split("-")
        for x in temp:
            if x in numbers:
                progList.append(numbers[x])

    if isinstance(progression, list):
        for x in progression:
            if x in numbers:
                progList.append(numbers[x])
    
    return progList

#Functions for testing
def printChords(chords):
    for x in chords:
        print(x)

def test():
    root1, root2, root3, root4, root5 = "Cmaj", "Amin", "C", "Hmaj", ""
    prog1 = "I-IV-V"
    prog2 = ["I", "IV", "V"]
    prog3 = []

    #explicit major root
    chords1 = get_progression(root1, prog1)
    #progression string
    chords2 = get_progression(root2, prog1)
    #progression array
    chords3 = get_progression(root2, prog2)
    #implicit major root
    chords4 = get_progression(root3, prog1)
    #invalid root
    chords5 = get_progression(root4, prog1)
    #empty root
    chords6 = get_progression(root5, prog1)
    #empty progression
    chords7 = get_progression(root4, prog3)

    printChords(chords1)
    printChords(chords2)
    printChords(chords3)
    printChords(chords4)
    printChords(chords5)
    printChords(chords6)
    printChords(chords7)

#Calls test function
test()
    

    