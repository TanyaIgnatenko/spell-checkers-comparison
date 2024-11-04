# Spell Checkers Comparison

## Overview

This research aims to compare various spell-checking tools and evaluate their work.

## Tools that were selected for the analysis:
- `PySpellChecker`
- `TextBlobChecker`
- `AutocorrectChecker`

## Dataset

### Birkbeck Dataset
This research uses the part of [the Birkbeck dataset](https://www.dcs.bbk.ac.uk/~ROGER/missp.dat) (3000 misspelled words and 3000 correct words).

## Metrics Used for Evaluation

The following metrics are utilized to assess the performance of each spell checker:

### 1. Accuracy
- **Definition**: The proportion of correctly identified words (both correct and misspelled) out of the total words processed.
- **Importance**: Provides a general measure of how well the spell checker performs overall.

### 2. Precision
- **Definition**: The ratio of true positive corrections (correctly identified misspellings) to the total number of words flagged as incorrect (true positives + false positives).
- **Importance**: Indicates how many of the flagged words were actually misspelled. High precision means fewer false alarms.

### 3. Recall
- **Definition**: The ratio of true positive corrections to the total number of actual misspellings in the text (true positives + false negatives).
- **Importance**: Measures how well the spell checker identifies all misspelled words. High recall means that most misspellings are caught.

### 4. F1 Score
- **Definition**: The harmonic mean of precision and recall.
- **Importance**: Provides a single score that balances both precision and recall, useful when you need to consider both false positives and false negatives.

### 5. Fix Rate
- **Definition**: The percentage of misspelled words that were correctly corrected by the spell checker.
- **Importance**: Directly measures the effectiveness of the spell checker in fixing errors.

### 6. Speed
- **Definition**: The number of words processed per second by the spell checker.
- **Importance**: Important for user experience, especially in real-time applications where quick feedback is necessary.

### 7. Error Type Detection Accuracy
- **Definition**: The accuracy with which different types of spelling errors (e.g., insertion, deletion, substitution) are detected and corrected.
- **Importance**: Helps identify strengths and weaknesses in handling specific types of errors.

## Report

You could read report [here](./Report.ipynb).

## Evalution script

You could see evalution script [here](./Spell_Checkers_Evaluation.ipynb).

## Generating dataset script

You could see generating dataset script [here](./format_dataset.py).

## Conclusion

The comparative analysis of the three spell checkers reveals distinct strengths and weaknesses for each tool:

- `PySpellChecker` excels in accuracy and precision but has a moderate fix rate, indicating effective identification but limited correction capabilities.
- `TextBlobChecker`, while having good precision, suffers from low accuracy and recall, making it less reliable for comprehensive spell-checking tasks.
- `AutocorrectChecker`, despite its high speed and balanced performance metrics, still needs improvements in recall to enhance its overall effectiveness.

In conclusion, while all three spell checkers have their merits, the choice of tool may depend on specific use cases—whether prioritizing speed, accuracy, or correction capability is more critical for the intended application in real-world scenarios.

## Usage

To replicate this research:
1. Clone this repository.
2. Ensure you have Python installed along with required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `textblob`, `pyspellchecker`, `autocorrect`).
3. Use the provided parts of Birkbeck dataset (`birkbeck_misspell.csv` and `birkbeck_correct.txt`) or create this files by your own from Birkbeck dataset by running command `python format_dataset.py`
(NOTE: Ensure that you downloaded Birkbeck dataset by yourself in this case and it has name "missp.dat.txt").
4. Run the "Spell_Checkers_Evaluation.ipynb" Juputer Notebook to see results and visualizations.