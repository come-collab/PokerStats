import re
import os

def parse_summary_sections(data):
    summaries = []
    current_summary = []
    in_summary_section = False

    for line in data:
        if '*** SUMMARY ***' in line:
            in_summary_section = True
            current_summary = [line]

        elif in_summary_section:
            if 'Winamax Poker -' in line and current_summary:
                summaries.append(''.join(current_summary))
                current_summary = []
                in_summary_section = False
            else:
                current_summary.append(line)

    if current_summary:
        summaries.append(''.join(current_summary))

    return summaries

def extract_winnings_for_player(summaries, player_name):
    winnings = []

    for summary in summaries:
        if f"{player_name} won" in summary:
            winnings.append(summary)

    return winnings

def calculate_total_winnings(winnings):
    total_winnings = 0.0

    for win in winnings:
        amount_won = re.search(r'won (\d+\.\d+)€', win)
        if amount_won:
            total_winnings += float(amount_won.group(1))

    return total_winnings

def count_active_preflop_hands(data, player_name):
    hand_count = 0
    in_hand = False
    pre_flop_section = False

    for line in data:
        if 'Winamax Poker -' in line:
            in_hand = False
            pre_flop_section = False

        if 'Dealt to ' + player_name in line:
            in_hand = True

        if in_hand and '*** PRE-FLOP ***' in line:
            pre_flop_section = True

        if pre_flop_section and player_name in line and 'folds' not in line:
            hand_count += 1
            in_hand = False

    return hand_count

# Usage
folder_path = 'daysOfPoker'
player_name = 'Fried Berg'
big_blind_size = 0.02  # Change this as per your game
overall_total_winnings = 0.0
overall_hand_count = 0

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Assuming all hand history files end with .txt
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()

        summaries = parse_summary_sections(data)
        fried_berg_winnings = extract_winnings_for_player(summaries, player_name)
        total_winnings = calculate_total_winnings(fried_berg_winnings)
        active_preflop_hand_count = count_active_preflop_hands(data, player_name)

        print(f"Total Winnings for {player_name} in {filename}: {total_winnings}")

        # Aggregate totals
        overall_total_winnings += total_winnings
        overall_hand_count += active_preflop_hand_count

# Calculating overall winrate in BB/100
overall_winrate_bb_per_100 = (overall_total_winnings / (overall_hand_count * big_blind_size)) * 100
overall_hand_count += active_preflop_hand_count
print(f"Overall Hands Played for {player_name}: {overall_hand_count}")
print(f"Overall Winrate for {player_name}: {overall_winrate_bb_per_100} BB/100")
