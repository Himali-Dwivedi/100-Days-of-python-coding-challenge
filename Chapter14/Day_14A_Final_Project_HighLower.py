# Write your code below this line 👇
import random;
import time;
import Day_14A_Final_Project_HigherLower_Data as data;
import Day_14A_Final_Project_HigherLower_Functions as functions;

does_player_win = True;
round = 1;
highscore = functions.load_high_score();
score = 0;

compare1 = random.choice(data.data);
compare2 = random.choice(data.data);

while (does_player_win == True):
    if(compare1 == compare2):
        continue;
    print("=" * 45);
    print("\t\t🎲 HIGHER OR LOWER 🎲");
    print("=" * 45);
    print(f"Round: {round}\tScore: {score}\tHigh score: {highscore}")
    print("-" * 45);
    print(f"\nDoes {compare2["name"]}, {compare2["description"]}, from {compare2["country"]} have higher or lower followers than {compare1["name"]}, {compare1["description"]}, from {compare1["country"]}?");
    print(f"[A] {compare1["name"]}\t->\t{compare1["follower_count"]}M");
    print(f"[B] {compare2["name"]}\t->\t???");
    print("-" * 45);

    user_input = input("Type [H] for Higher or [L] for Lower: ")
    while(user_input.upper() not in ["L", "H"]):
        user_input = input("Invalid input! Type [H] for Higher or [L] for Lower: ");
    
    if(user_input.upper() == "H"):
        if(compare2["follower_count"] > compare1["follower_count"]):
            functions.clear();
            score += 1;
            functions.print_results(round = round, score = score, highscore = highscore, compare1 = compare1, compare2 = compare2);
            print(f"✅ Correct! {compare2["name"]} has HIGHER followers.");
            time.sleep(5);
            functions.clear();
            compare1 = compare2;
            compare2 = random.choice(data.data);
        else:
            functions.clear();
            functions.print_results(round = round, score = score, highscore = highscore, compare1 = compare1, compare2 = compare2);
            print(f"❌ Wrong! {compare2["name"]} has LOWER followers.");
            print("Game Over!")
            break;
    elif(user_input.upper() == "L"):
        if(compare2["follower_count"] < compare1["follower_count"]):
            functions.clear();
            score += 1;
            functions.print_results(round = round, score = score, highscore = highscore, compare1 = compare1, compare2 = compare2);
            print(f"✅ Correct! {compare2["name"]} has LOWER followers.");
            time.sleep(5);
            functions.clear();
            compare2 = random.choice(data.data);
        else:
            functions.clear();
            functions.print_results(round = round, score = score, highscore = highscore, compare1 = compare1, compare2 = compare2);
            print(f"❌ Wrong! {compare2["name"]} has HIGHER followers.");
            print("Game Over!");
            break; 
    round +=1;
    
if(score > highscore):
    functions.save_high_score(score = score);
    print("Well done! That's a new high score!");