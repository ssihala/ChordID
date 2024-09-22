from pychord import Chord

#Calls pychord function and returns all notes in a chords object
def get_progression(root, progression):
    progList, chords = [], []

    progList = romanToInt(progression)

    for x in progList:
        note = Chord.from_note_index(x, "", root, diatonic=True)
        chords.append(note)

    return chords

#Converting Roman Numerals into Integars
def romanToInt (progression):
    progList = []

    numbers = {
        "I": 1, "II": 2, "III": 3, 
        "IV": 4, "V": 5, "VI": 6, 
        "VII": 7, "VIII": 8, "IX": 9, 
        "X": 10, "XI": 11
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
    root1, root2 = "Cmaj", "Amin"
    prog1 = "I-IV-V"
    prog2 = ["I", "IV", "V"]

    chord1 = get_progression(root1, prog1)
    chord2 = get_progression(root2, prog1)
    chord3 = get_progression(root2, prog2)

    printChords(chord1)
    printChords(chord2)
    printChords(chord3)

#Calls test function
test()
    

    