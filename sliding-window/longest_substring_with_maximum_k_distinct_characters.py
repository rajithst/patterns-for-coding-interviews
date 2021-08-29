given_string = "araaci"
window_start = 0
max_length = 0
distinct_characters = 2

#keep track of each caracter count
character_frequency = {}

#iterate over each caracter as window end point
for window_end in range(len(given_string)):

    character = given_string[window_end]
    #if character already in dict update count,else add to the dict
    if character not in character_frequency:
        character_frequency[character] = 0
    character_frequency[character] += 1

    #if distinct character count is more than expected count,move the start window point forward till distinct count is expected value
    while len(character_frequency) > distinct_characters:
        remove_character = given_string[window_start]
        character_frequency[remove_character] -= 1
        if character_frequency[remove_character] == 0:
            del character_frequency[remove_character]
        window_start += 1
    max_length = max(max_length,window_end-window_start+1)
