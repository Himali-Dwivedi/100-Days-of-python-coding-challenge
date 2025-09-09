# Write your code below this line 👇
# Write a program that sums up the list of numbers
student_scores = [180, 124, 165, 173, 189, 169, 146];

# Approach 1:
print(f"Approach 1: sum of student scores is {sum(student_scores)}");

#Approach 2
sum = 0
for score in student_scores:
    sum += score;
print(f"Approach 2: Sum of student scores is {sum}");


#Write a program that returns the highest score from the list
student_scores = [180, 124, 165, 173, 189, 169, 146];

#Approach 1:
print(f"Approach 1: The highest score in the list is {max(student_scores)}");

#Approach 2:
highest_score = 0;
for score in student_scores:
    if(score > highest_score):
        highest_score = score;
print(f"Approach 2: The highest score in the list is {highest_score}");