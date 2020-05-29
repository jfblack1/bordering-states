
stateMap = {
    "Alabama": ["Florida", "Georgia", "Mississippi", "Tennessee"],
    "Alaska": [],
    "Arizona": ["California", "Nevada", "New Mexico", "Utah"],
    "Arkansas": ["Louisiana", "Mississippi", "Missouri", "Oklahoma", "Tennessee", "Texas"],
    "California": ["Oregon", "Nevada", "Arizona"],
    "Colorado": ["Kansas", "Oklahoma", "Nebraska", "New Mexico", "Utah", "Wyoming"],
    "Connecticut": ["Massachusetts", "New York", "Rhode Island"],
    "Delaware": ["Pennsylvania", "Maryland", "New Jersey"],
    "Florida": ["Alabama", "Georgia"],
    "Georgia": ["Alabama", "Florida", "North Carolina", "South Carolina", "Tennessee"],
    "Hawaii": [],
    "Idaho": ["Oregon", "Nevada", "Montana", "Utah", "Washington", "Wyoming"],
    "Illinois": ["Indiana", "Iowa", "Kentucky", "Michigan", "Missouri", "Wisconsin"],
    "Indiana": ["Illinois", "Kentucky", "Michigan", "Ohio"],
    "Iowa": ["Illinois", "Minnesota", "Missouri", "Nebraska", "South Dakota", "Wisconsin"],
    "Kansas": ["Colorado", "Missouri", "Nebraska", "Oklahoma"],
    "Kentucky": ["Illinois", "Indiana", "Missouri", "Ohio", "Tennessee", "Virginia", "West Virginia"],
    "Louisiana": ["Arkansas", "Mississippi", "Texas"],
    "Maine": ["New Hampshire"],
    "Maryland": ["Delaware", "Pennsylvania", "Virginia", "West Virginia"],
    "Massachusetts": ["Connecticut", "New Hampshire", "New York", "Rhode Island", "Vermont"],
    "Michigan": ["Illinois", "Indiana", "Minnesota", "Ohio", "Wisconsin"],
    "Minnesota": ["Iowa", "Michigan", "North Dakota", "South Dakota", "Wisconsin"],
    "Mississippi": ["Alabama", "Arkansas", "Louisiana", "Tennessee"],
    "Missouri": ["Arkansas", "Illinois", "Iowa", "Kansas", "Kentucky", "Nebraska", "Oklahoma", "Tennessee"],
    "Montana": ["Idaho", "North Dakota", "South Dakota", "Wyoming"],
    "Nebraska": ["Colorado", "Iowa", "Kansas", "Missouri", "South Dakota", "Wyoming"],
    "Nevada": ["Arizona", "California", "Idaho", "Oregon", "Utah"],
    "New Hampshire": ["Maine", "Massachusetts", "Vermont"],
    "New Jersey": ["Delaware", "Pennsylvania", "New Jersey"],
    "New Mexico": ["Arizona", "Colorado", "Oklahoma", "Texas"],
    "New York": ["Connecticut", "Massachusetts", "New Jersey", "Pennsylvania", "Vermont"],
    "North Carolina": ["Georgia", "Tennessee", "South Carolina", "Virginia"],
    "North Dakota": ["Minnesota", "Montana", "South Dakota"],
    "Ohio": ["Indiana", "Kentucky", "Michigan", "Pennsylvania", "West Virgina"],
    "Oklahoma": ["Arkansas", "Colorado", "Kansas", "Missouri", "New Mexico", "Texas"],
    "Oregon": ["California", "Idaho", "Nevada", "Washington"],
    "Pennsylvania": ["Delaware", "Maryland", "New Jersey", "New York", "Ohio", "West Virginia"],
    "Rhode Island": ["Connecticut", "Massachusetts"],
    "South Carolina": ["Georgia", "North Carolina"],
    "South Dakota": ["Iowa", "Minnesota", "Montana", "Nebraska", "North Dakota", "Wyoming"],
    "Tennessee": ["Alabama", "Arkansas", "Georgia", "Kentucky", "Mississippi", "Missouri", "North Carolina", "Virginia"],
    "Texas": ["Arkansas", "Louisiana", "New Mexico", "Oklahoma"],
    "Utah": ["Arizona", "Colorado", "Idaho", "Nevada", "Wyoming"],
    "Vermont": ["Massachusetts", "New Hampshire", "New York"],
    "Virginia": ["Kentucky", "Maryland", "North Carolina", "Tennessee", "West Virginia"],
    "Washington": ["Idaho", "Oregon"],
    "West Virginia": ["Kentucky", "Maryland", "Ohio", "Pennsylvania", "Virginia"],
    "Wisconsin": ["Illinois", "Iowa", "Michigan", "Minnesota"],
    "Wyoming": ["Colorado", "Idaho", "Nebraska", "Montana", "South Dakota", "Utah"]
    }

def getBoarderStates (state):
    boarderStates = stateMap.get(state, "")
    result = "The states that boarder " + state + " are "
    i = 0
    for state in boarderStates:
        if (i >= len (boarderStates) - 1):
            result += "and " + state + "."
        else:
            result += state + ", "
        i+=1
    return result

def askQuestion ():
    while (True):
        print ("Enter a state to find out which states border it: ", end="")
        state = input()
        print (getBoarderStates(state))
        c = input ("Continue? (yes/no): ")
        if (c == "no"):
            break
    
askQuestion()
    