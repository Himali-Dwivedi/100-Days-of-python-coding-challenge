# Write your code below this line 👇
import os;
# Save high score to a file
def save_high_score(score, filename="Chapter14/Day_14A_Final_Project_HigherLower_Highscore.txt"):
    with open(filename, "w") as f:
        f.write(str(score))

# Load high score from a file
def load_high_score(filename="Chapter14/Day_14A_Final_Project_HigherLower_Highscore.txt"):
    try:
        with open(filename, "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        print("File not found");
        return 0  # no high score yet

def print_results(round, score, highscore, compare1, compare2):
    print("=" * 45);
    print("\t\t🎲 HIGHER OR LOWER 🎲");
    print("=" * 45);
    print(f"Round: {round}\tScore: {score}\tHigh score: {highscore}")
    print("-" * 45);
    print(f"\nDoes {compare2["name"]}, {compare2["description"]}, from {compare2["country"]} have higher or lower followers than {compare1["name"]}, {compare1["description"]}, from {compare1["country"]}?");
    print(f"[A] {compare1["name"]}\t->\t{compare1["follower_count"]}M");
    print(f"[B] {compare2["name"]}\t->\t{compare2["follower_count"]}M");
    print("-" * 45);

def clear():
    if(os.name == "nt"):
        os.system("cls");
    else:
        os.system("clear");
