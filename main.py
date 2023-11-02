import xml.etree.ElementTree as ET
import random
import pygtrie as trie

def main():
    # read from kotus-sanalista_v1.xml
    input_path = "kotus-sanalista_v1/work_wordlist.xml"

    # parse the XML file
    tree = ET.parse(input_path)
    root = tree.getroot()

    eight_letter_words = set()

    # loop through all s elements
    for st in root.iter('st'):        
        text = st[0].text.replace("-", "")        
        # if word ends in nen, change it to end with set
        if text[-3:] == "nen" and len(text) == 8:
            eight_letter_words.add(text[:-3] + "set")

        t_element = st.find("t")
        if t_element is not None:
            tn_element = t_element.find("tn")
            if tn_element is not None:
                tn = tn_element.text
                if tn == "10" and len(text) == 7:
                    eight_letter_words.add(text + "t")
            
        if (len(text) == 8):                        
            eight_letter_words.add(text)
        

    # copy all items from trie to list original_words and shuffle it.
    original_words = list(eight_letter_words)
    random.shuffle(original_words)

    # create a new set of eight letter words that skips first two and last two characters.
    eight_letter_words_without_ends = set()
    for word in original_words:
        eight_letter_words_without_ends.add(word[2:-2])

    horizontal_words = []
    vertical_words = []

    # horizontal words.
    while len(original_words) > 0 and len(horizontal_words) < 4:          
        # pop first word from original_words and add it to horizontal_words
        word_candidate = original_words.pop()
        eight_letter_words.remove(word_candidate)
        
        # concatenate horizontal_words items third characters to variable combined.
        combined = ""
        for word in horizontal_words:
            combined += word[2]
        # add third character of word_candidate to combined.
        combined += word_candidate[2]

        # store to variable possible_words all words that start with combined in eight_letter_words_without_ends.
        possible_words = []
        for word in eight_letter_words_without_ends:
            if word.startswith(combined):
                possible_words.append(word)
                if len(possible_words) > (4 - len(combined)):
                    break
        # if possible_words is greater than 3, add word_candidate to horizontal_words.
        if len(possible_words) > (4 - len(combined)):
            horizontal_words.append(word_candidate)

    # vertical words.
    current_index = 0
    while (len(original_words) > 0 and len(vertical_words < 4)):
        # from horizontal_words, get character at index current_index + 2 and store it to variable combined.
        combined = ""
        for word in horizontal_words:
            combined += word[current_index + 2]
        break






        
        
        
        

    
        




    

        

    

    

if __name__ == "__main__":
    main()