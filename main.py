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
        eight_letter_words_without_ends.add(word[2:-3])
        eight_letter_words_without_ends.add(word[2:-4])
        eight_letter_words_without_ends.add(word[2:-5])

    horizontal_words = []
    vertical_words = []

    # horizontal words.
    while len(original_words) > 0 and len(horizontal_words) < 4:          
        # pop first word from original_words and add it to horizontal_words
        word_candidate = original_words.pop()
        eight_letter_words.remove(word_candidate)
        
        first_word_fits = check_that_nth_index_word_fits(word_candidate, 2, horizontal_words, eight_letter_words_without_ends)
        if first_word_fits:
            second_word_fits = check_that_nth_index_word_fits(word_candidate, 3, horizontal_words, eight_letter_words_without_ends)
            if second_word_fits:
                third_word_fits = check_that_nth_index_word_fits(word_candidate, 4, horizontal_words, eight_letter_words_without_ends)
                if third_word_fits:
                    fourth_word_fits = check_that_nth_index_word_fits(word_candidate, 5, horizontal_words, eight_letter_words_without_ends)
                    if fourth_word_fits:
                        horizontal_words.append(word_candidate)            
    
    print(horizontal_words)

    if (len(horizontal_words) < 4):
        print("Not enough horizontal words found.")
        return

    # vertical words.
    while len(vertical_words) < 1:
        # combine third letters of horizontal words to variable combined.
        combined = ""
        for word in horizontal_words:
            combined += word[2]
            
        # find such a word from eight_letter_words that has combined as its 3rd, 4th, 5th and 6th characters.
        for word in eight_letter_words:
            if word[2:6] == combined:
                vertical_words.append(word)
                eight_letter_words.remove(word)
                break
    
    while len(vertical_words) < 2:
        # combine fourth letters of horizontal words to variable combined.
        combined = ""
        for word in horizontal_words:
            combined += word[3]

        # find such a word from eight_letter_words that has combined as its 3rd, 4th, 5th and 6th characters.
        for word in eight_letter_words:
            if word[2:6] == combined:
                vertical_words.append(word)
                eight_letter_words.remove(word)
                break

    while len(vertical_words) < 3:
        # combine fifth letters of horizontal words to variable combined.
        combined = ""
        for word in horizontal_words:
            combined += word[4]

        # find such a word from eight_letter_words that has combined as its 3rd, 4th, 5th and 6th characters.
        for word in eight_letter_words:
            if word[2:6] == combined:
                vertical_words.append(word)
                eight_letter_words.remove(word)
                break

    while len(vertical_words) < 4:
        # combine sixth letters of horizontal words to variable combined.
        combined = ""
        for word in horizontal_words:
            combined += word[5]

        # find such a word from eight_letter_words that has combined as its 3rd, 4th, 5th and 6th characters.
        for word in eight_letter_words:
            if word[2:6] == combined:
                vertical_words.append(word)
                eight_letter_words.remove(word)
                break

    print(vertical_words)

    if (len(vertical_words) < 4):
        print("Not enough vertical words found.")
        return
    
    # print 4x8 table. Each row contains one of the horizontal words so that each td contains one character of the word upper cased.
    print("<table>")
    for word in horizontal_words:
        print("<tr>")
        for character in word:
            print("<td>" + character.upper() + "</td>")
        print("</tr>")
    print("</table>")
    
 
def check_that_nth_index_word_fits(word_candidate, n, horizontal_words, eight_letter_words_without_ends):
    # concatenate horizontal_words items nth characters to variable combined.
    combined = ""
    for word in horizontal_words:
        combined += word[n]
    # add third character of word_candidate to combined.
    combined += word_candidate[n]

    # store to variable possible_words all words that start with combined in eight_letter_words_without_ends.
    possible_words = []
    if combined in eight_letter_words_without_ends:
        return True
    return False




        
        
        
        

    
        




    

        

    

    

if __name__ == "__main__":
    main()