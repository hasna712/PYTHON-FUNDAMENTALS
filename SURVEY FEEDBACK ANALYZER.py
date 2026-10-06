                # SURVEY FEEDBACK ANALYZER


#PRELOADED FEEDBACKS

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support,   not happy   ',
        'GREAT experience! will come again.',
        'okay   okay...',
        ' not   BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# ADD MORE FEEDBACKS

def add_feedbacks(data):
    
    while True:
        count_input = input("How many more feedbacks do you want to add? ")
        if count_input.isdigit():
            count = int(count_input)
            break
        print("Please enter a valid whole number.")

    for i in range(count):
        print(f"\n--- Feedback {i + 1} of {count} ---")

        name = input("Enter Name: ").strip()
        feedback = input("Enter Written Feedback: ")

        while True:
            rating_input = input("Enter Rating (1-5): ")
            if rating_input.isdigit() and 1 <= int(rating_input) <= 5:
                rating = int(rating_input)
                break
            print("Invalid rating. Please enter a number between 1 and 5.")

        
        new_s_no = data['S_No'][-1] + 1

       
        data['S_No'].append(new_s_no)
        data['Name'].append(name)
        data['Feedback'].append(feedback)
        data['Rating'].append(rating)

    print(f"\n{count} feedback(s) added. Total feedbacks: {len(data['S_No'])}")


add_feedbacks(feedback_data)

print(feedback_data)


# TEXT CLEANING


def clean_text(text):
   
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')
    
    text = text.lower()
    return ' '.join(text.split())


cleaned_list = []
for fb in feedback_data['Feedback']:
    cleaned_list.append(clean_text(fb))
feedback_data['Feedback'] = cleaned_list


#WORD COUNT INSIGHTS

def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        if word in fb.split():  
            count += 1
    return count


print("\n--- Word Count Insights ---")
print('Number of feedbacks containing "good":', count_word_in_feedbacks("good"))
print('Number of feedbacks containing "poor":', count_word_in_feedbacks("poor"))
print('Number of feedbacks containing "excellent":', count_word_in_feedbacks("excellent"))


#FINAL SUMMARY & INSIGHTS


print("\n--- Final Cleaned feedback_data ---")
for key in feedback_data:
    print(f"{key}: {feedback_data[key]}")


average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage Rating:", round(average_rating, 2))


longest_index = 0
max_words = 0
for i in range(len(feedback_data['Feedback'])):
    word_count = len(feedback_data['Feedback'][i].split())
    if word_count > max_words:
        max_words = word_count
        longest_index = i

print("\nLongest Comment:")
print("Name    :", feedback_data['Name'][longest_index])
print("Feedback:", feedback_data['Feedback'][longest_index])
print("Words   :", max_words)


unique_words = set()
for fb in feedback_data['Feedback']:
    for w in fb.split():
        unique_words.add(w)

print("\nUnique Words:", sorted(unique_words))
print("Total unique words:", len(unique_words))


print("\n--- Feedbacks Sorted by Rating (High to Low) ---")
combined = zip(feedback_data['S_No'], feedback_data['Name'],
               feedback_data['Feedback'], feedback_data['Rating'])
sorted_entries = sorted(combined, key=lambda x: x[3], reverse=True)

for s_no, name, fb, rating in sorted_entries:
    print(f"{s_no:<3} {name:<8} Rating: {rating}  {fb}")
