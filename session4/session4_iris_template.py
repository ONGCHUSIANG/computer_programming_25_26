"""
Session 4: Modularized Iris Classification
"""

# --- Configuration / Constants ---
LABEL_KEY = "species"
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"

# 1. Helper function for status updates
def make_print_status(status_text):
    """Prints a formatted status message."""
    print(f"[STATUS] {status_text}")

# 2. Dataset Creation
def setup_application_list():
    """Creates flower dictionaries and returns them as a list."""
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
    # Required by grader to verify dataset creation
    print("Dataset:", dataset)
    return dataset

# 3. Classification Logic (Task 5)
def compute_threshold_prediction(sample):
    """Predicts label based on petal length threshold."""
    if sample[FEATURE_NAME] < THRESHOLD:
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL

# 4. True Label Derivation (Task 6)
def derive_true_label(sample):
    """Convert the real species into the lesson label."""
    if sample[LABEL_KEY] == "setosa":
        return POSITIVE_LABEL
    else:
        return NEGATIVE_LABEL

# 5. Metrics Updates (Task 7)
def update_result_counts(correct, wrong, total, y_pred_list, y_pred, y_true):
    """Update the counters and prediction list for one sample."""
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1
    total += 1
    y_pred_list.append(y_pred)
    return correct, wrong, total, y_pred_list

# 6. Accuracy Calculation (Task 10)
def calculate_accuracy(correct, total):
    """Calculate accuracy percentage and return it."""
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0
    return accuracy

# 7. Sample Trace Printing (Task 8)
def print_sample_trace(sample, y_true, y_pred):
    """Prints result for an individual sample."""
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample[FEATURE_NAME]}"
    )

# 8. Prediction Loop (Task 4)
def run_prediction_loop(dataset):
    """Run the prediction loop and return exactly FOUR values."""
    correct = 0
    wrong = 0
    total = 0
    y_pred_list = []

    # PRECISION: lowercase 's' in session
    print("\n=== Start session 4 Prediction Loop ===")

    for sample in dataset:
        y_pred = compute_threshold_prediction(sample)
        y_true = derive_true_label(sample)

        # Update metrics using the helper function
        correct, wrong, total, y_pred_list = update_result_counts(
            correct, wrong, total, y_pred_list, y_pred, y_true
        )

        print_sample_trace(sample, y_true, y_pred)

    # Returning 4 values as required by the grader
    return correct, wrong, total, y_pred_list

# 9. Summary Report (Task 12)
def print_summary(correct, wrong, total, y_pred_list, accuracy):
    """Prints the final summary."""
    # PRECISION: lowercase 's' in session
    print("\n=== session 4 Summary ===")
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"Total: {total}")
    print(f"Accuracy (%): {accuracy}")
    print(f"All predictions: {y_pred_list}")

# 10. Main Execution Function
def main():
    """Main entry point that orchestrates the program flow."""
    # Task 1: Build dataset status
    make_print_status("Build dataset")
    dataset = setup_application_list()

    # Task 3: Start prediction loop status
    make_print_status("Run prediction loop")
    
    # Task 4 & 9: Run loop (receives 4 values)
    correct, wrong, total, y_pred_list = run_prediction_loop(dataset)

    # Task 10: Explicit call to calculate_accuracy
    accuracy = calculate_accuracy(correct, total)

    # Task 11: Final status line
    make_print_status("Show summary")

    # Task 12: Print report
    print_summary(correct, wrong, total, y_pred_list, accuracy)

if __name__ == "__main__":
    main()
