

# Session 2 continuity variables (Rule settings). Do not change these.
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"



correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made


flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower

flower2 = {
"id": "flower2",
"sepal_length": 4.9,
"sepal_width": 3.0,
"petal_length": 1.4,
"petal_width": 0.2,
"species": "setosa"
} #remember to close me for a dict


# Task 2: Create list of dictionaries
dataset= [flower1, flower2]
threshold = 2.0             # Common threshold for Iris Setosa petal length
positive_label = "setosa"
negative_label = "not setosa"

# Task 3: Create a for loop to process the dataset
for sample in dataset:
    # 1. Identify true label
    y_true = sample["species"]

    # 2. Classification logic
    if sample["petal_length"] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label

    # 3. Update Metrics (CRITICAL)
    total += 1
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1
    
    # 4. Append prediction to the list
    y_pred_list.append(y_pred)

    # Task 4: Print Per-Sample Trace Line (Exact format from manual)
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample['petal_length']}"
    )

# --- THE SUMMARY (Task 5 - After the loop) ---
accuracy = (correct / total) * 100 if total > 0 else 0.0

print("-" * 30) # Visual separator
print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Total: {total}")
print(f"Accuracy (%): {accuracy}")
print(f"All predictions: {y_pred_list}")