import csv

TARGET_WORDS_COUNT = 3000

# Determine the type of error between the correct and misspelled words.
def determine_error_type(correct, misspelled):
    if len(correct) < len(misspelled):
        return 'insertion'
    elif len(correct) > len(misspelled):
        return 'deletion'
    elif len(correct) == len(misspelled):
        # Check for transposition
        diff_count = sum(1 for a, b in zip(correct, misspelled) if a != b)
        if diff_count == 2 and sorted(correct) == sorted(misspelled):
            return 'transposition'
        else:
            return 'substitution'
    return 'unknown'

def process_birkbeck_dataset(input_file, output_incorrect_file, output_correct_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    correct_word = ''
    correct_words = set()  # To track unique correct words written
    incorrect_words = []
    
    # Write file with incorrect words
    with open(output_incorrect_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['correct_word', 'misspelling', 'error_type', 'source'])

        for line in lines:
            line = line.strip()
            if line.startswith('$'):
                correct_word = line[1:].replace('_', ' ')
            elif line and correct_word:
                misspelling = line.replace('_', ' ')
                error_type = determine_error_type(correct_word, misspelling)

                if (len(incorrect_words) < TARGET_WORDS_COUNT):
                    csvwriter.writerow([correct_word, misspelling, error_type, "birkbeck"])
                    incorrect_words.append(misspelling)    
                correct_words.add(correct_word)
    
    # Write file with correct words
    with open(output_correct_file, 'w', encoding='utf-8') as output_file:
        for index, correct in enumerate(correct_words):
            if index == TARGET_WORDS_COUNT:
                break

            output_file.write(f'{correct}\n')

input_file = "./missp.dat.txt" 
output_incorrect_csv = "birkbeck_misspell.csv"
output_correct_txt = "birkbeck_correct.txt"

process_birkbeck_dataset(input_file, output_incorrect_csv, output_correct_txt)

print(f"Formatted data has been written to {output_incorrect_csv} and {output_correct_txt}")