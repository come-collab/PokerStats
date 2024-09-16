# PokerStats
This repository will contain multiple Python script that will help you to analyse in a better way your stats.

## Winamax Hand History
### Poker Hand History Analyzer (you can find it ine the file : poker-winrate-winamax.py)

This script analyzes poker hand history data for a specific player ("Your Name") across multiple text files. Each file contains a series of poker hands. The script performs the following functions:

1. **Extract Hand Summaries**: It identifies and extracts the summary section from each hand, focusing on the player's winnings.

2. **Count Active Pre-Flop Hands**: Counts the number of hands where the player was active during the pre-flop stage (excluding hands where the player only folded).

3. **Calculate Total Winnings**: Aggregates the total winnings from all hands where the player won.

4. **Overall Winrate Calculation**: The winrate is calculated using the formula: Winrate (BB/100) = (Total Winnings / Total Active Hands) * (100 / Big Blind Size).

5. **Upload your files to the DayOfPoker folder (all your hands per day) you can also create your own folder but just change the folder name in the code and change the name of the player and the BB (at the end of the code)** 
