"""
Session 4: Modularized Iris Classification
This version converts the Session 3 logic into standalone functions 
to improve readability and organization.
"""

# --- Configuration / Constants ---
LABEL_KEY = "species"
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"

# Task 1: Helper function for status updates
def make_print_status(status_text):
    """Prints a formatted status message."""
    print(f"[STATUS] {status_text}")

# Task 2: Dataset Creation
def setup_application_list():
    """Creates individual flower dictionaries and returns them as a list."""
    flower1 = {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

    flower2 = {
        "id": "flower2",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

    dataset = [flower1, flower2]
    return dataset

# Task 5: Classification Logic
def compute_threshold_prediction(sample):
    """Predicts label based on petal length threshold."""
    if sample[FEATURE_NAME] < THRESHOLD:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL

# Task 6: True Label Derivation
def derive_true_label(sample):
    """Converts the dataset species into our specific lesson labels."""
    if sample[LABEL_KEY] == "setosa":
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL

# Task 7: Metrics Updates
def update_result_counts(correct, wrong, total, y_pred_list, y_pred, y_true):
    """Updates counters and prediction history."""
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    total += 1
    y_pred_list.append(y_pred)
    return correct, wrong, total, y_pred_list

# Task 10: Accuracy Calculation
def calculate_accuracy(correct, total):
    """Calculates accuracy as a percentage."""
    if total > 0:
        return (correct / total) * 100
    return 0.0

# Task 8: Sample Trace Printing
def print_sample_trace(sample, y_true, y_pred):
    """Prints the result for an individual sample."""
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample[FEATURE_NAME]}"
    )

# Tasks 4-9: Prediction Loop
def run_prediction_loop(dataset):
    """Orchestrates the prediction process for the entire dataset."""
    correct = 0
    wrong = 0
    total = 0
    y_pred_list = []

    print("\n=== Start Session 4 Prediction Loop ===")

    for sample in dataset:
        # Task 5: Predict
        y_pred = compute_threshold_prediction(sample)

        # Task 6: Get True Label
        y_true = derive_true_label(sample)

        # Task 7: Update Metrics
        correct, wrong, total, y_pred_list = update_result_counts(
            correct, wrong, total, y_pred_list, y_pred, y_true
        )

        # Task 8: Display results
        print_sample_trace(sample, y_true, y_pred)

    return correct, wrong, total, y_pred_list

# Task 12: Summary Report
def print_summary(correct, wrong, total, y_pred_list, accuracy):
    """Prints the final results summary."""
    print("\n=== Session 4 Summary ===")
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"Total: {total}")
    print(f"Accuracy (%): {round(accuracy, 2)}")
    print(f"All predictions: {y_pred_list}")

# Main Execution Function
def main():
    """Runs the full classification pipeline."""
    # Step 1: Setup
    make_print_status("Building dataset...")
    dataset = setup_application_list()

    # Step 2: Predict
    make_print_status("Running prediction loop...")
    correct, wrong, total, y_pred_list = run_prediction_loop(dataset)

    # Step 3: Metrics
    accuracy = calculate_accuracy(correct, total)

    # Step 4: Report
    make_print_status("Generating final summary...")
    print_summary(correct, wrong, total, y_pred_list, accuracy)

if __name__ == "__main__":
    main()
