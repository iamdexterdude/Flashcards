Flashy is an interactive flashcard-based language learning application designed to help users expand their vocabulary effectively. It uses a simple, intuitive interface to display German words with their Uzbek translations, making the language learning experience engaging and user-friendly.

Features
Flashcard Display: Each card shows a German word, which can be flipped to reveal its Uzbek translation.
Progress Tracking: Users can mark words as "learned," and these words are removed from the pool of unlearned words.
Dynamic Data Management: The app saves progress by storing unlearned words in a CSV file, ensuring continuity across sessions.
Fallback Mechanism: If no saved progress file is found or it’s empty, the app initializes with the original dataset.
How to Use
Start the App: Run the program to load the flashcard interface.
Review Words: German words appear on the front of the card. Use the buttons to interact:
Flip Card: See the Uzbek translation by clicking the "Wrong" button.
Mark as Learned: Remove a word from the pool by clicking the "Right" button.
Complete the Set: Once all words are learned, the app congratulates you on completing the session.
Requirements
Python 3.x
Tkinter (GUI Library)
Pandas (for CSV file handling)
A directory structure containing the following files:
./data/german-uzbek.csv (Original dataset)
./images/card_front.png (Card front design)
./images/card_back.png (Card back design)
./images/right.png and ./images/wrong.png (Button images)
Setup
Clone the repository.
Place the necessary images and the dataset in their respective directories.
Install the required dependencies:
bash

pip install pandas
Run the script:
bash

python flashy.py
Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. For major changes, please open an issue first to discuss potential enhancements.

License
This project is licensed under the MIT License.

