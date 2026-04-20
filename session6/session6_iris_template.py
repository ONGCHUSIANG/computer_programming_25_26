"""Session 6 student template: Classes and Objects.

In this session, you will refactor the Session 5 functional pipeline
into a class called IrisRuleClassifier. This class bundles configuration
(threshold and labels) and behavior (prediction and evaluation) together.

How to run:
    python3 session6/session6_iris_template.py
"""


from asyncio import Task


def setup_application_list():
    """Return the dataset as a list of flower dictionaries.

    This function is provided for you. Do not modify it.
    """
    return [
        {"id": "flower1", "petal_length": 1.4, "species": "setosa"},
        {"id": "flower2", "petal_length": 1.5, "species": "setosa"},
        {"id": "flower3", "petal_length": 1.3, "species": "setosa"},
        {"id": "flower4", "petal_length": 4.5, "species": "versicolor"},
        {"id": "flower5", "petal_length": 4.7, "species": "versicolor"},
        {"id": "flower6", "petal_length": 5.1, "species": "virginica"},
        {"id": "flower7", "petal_length": 6.0, "species": "virginica"},
    ]


class IrisRuleClassifier:
    """A class that bundles configuration and prediction/evaluation behavior.

    Configuration (threshold, labels) is stored as attributes on self.
    Behavior (prediction, evaluation) is implemented as methods.
    """

    # Task 1: Define the __init__ Method
    def __init__(self, threshold=2.0): 
        """Store configuration inside the object."""
        self.threshold = threshold
        self.positive_label = "setosa"
        self.negative_label = "not_setosa"

    def print_status(self, status_text):
        """Print a small status message."""
        print(f"[STATUS] {status_text}")

    # Task 2: Implement compute_threshold_prediction
    def compute_threshold_prediction(self, sample):
        """Predict the label for one flower sample using the threshold rule."""
        if sample["petal_length"] < self.threshold:
            return self.positive_label
        else:
            return self.negative_label

    # Task 3: Implement derive_true_label
    def derive_true_label(self, sample):
        """Convert the real species name into the lesson label."""
        # Using self.positive_label instead of hardcoding "setosa"
        if sample["species"] == self.positive_label:
            return self.positive_label
        else:
            return self.negative_label
        

    # Task 4: Implement update_result_counts
    def update_result_counts(self, correct, wrong, total, y_pred_list, y_pred, y_true):
        """Update the running totals and prediction history for one sample."""
        
        # 1 & 2. Compare prediction to truth and update counters
        if y_pred == y_true:
            correct += 1
        else:
            wrong += 1
            
        # 3. Always increment the total processed
        total += 1
        
        # 4. Save the prediction to our history list
        y_pred_list.append(y_pred)
        
        # 5. Return the updated values as a tuple
        return correct, wrong, total, y_pred_list

    # Task 5: Implement calculate_accuracy
    def calculate_accuracy(self, correct, total):
        """Calculate accuracy as a percentage.

        Args:
            correct (int): Number of correct predictions.
            total (int): Total number of samples processed.

        Returns:
            float: Accuracy percentage between 0.0 and 100.0.
                   Returns 0.0 if total is zero (protect against division by zero).
        """
        # If total > 0:
        #     return (correct / total) * 100
        # Otherwise return 0.0 to avoid dividing by zero
        if total > 0:
            return(correct / total) * 100
        return 0.0

    # Task 6: Implement run_prediction_loop
    def run_prediction_loop(self, dataset):
        """Run prediction and evaluation on the full dataset.

        This method calls compute_threshold_prediction, derive_true_label,
        and update_result_counts for each sample in the dataset.
        Methods inside the same class can call each other using self.

        Args:
            dataset (list): A list of flower sample dictionaries.

        Returns:
            tuple: (correct, wrong, total, y_pred_list)
        """
        correct = 0
        wrong = 0
        total = 0
        y_pred_list = []

        print("\n=== Start Session 6 Prediction Loop ===")

        for sample in dataset:
            
            y_pred = self.compute_threshold_prediction(sample)
            y_true = self.derive_true_label(sample)
            
            correct, wrong, total, y_pred_list = self.update_result_counts(
                correct, wrong, total, y_pred_list, y_pred, y_true
            )
            
            print(
                f"id={sample['id']} | true={y_true} | pred={y_pred} | "
                f"petal_length={sample['petal_length']}"
            )

        return correct, wrong, total, y_pred_list

    # Task 7: Implement print_summary
    def print_summary(self, correct, wrong, total, y_pred_list, accuracy):
        """Print the final results after the prediction loop.

        Args:
            correct (int): Number of correct predictions.
            wrong (int): Number of wrong predictions.
            total (int): Total samples processed.
            y_pred_list (list): All predictions made.
            accuracy (float): Accuracy percentage.
        """
        print("\n=== Session 6 Summary ===")
        print("Correct:", correct)
        print("Wrong:  ", wrong)
        print("Total:  ", total)
        print("Accuracy (%):", round(accuracy, 2))
        print("All predictions:", y_pred_list)


def main():

    # Step 1a: Create a classifier object with a chosen threshold
    classifier = IrisRuleClassifier(threshold=2.0)
    print("Threshold:", classifier.threshold)
    print("Positive label:", classifier.positive_label)
    print("Negative label:", classifier.negative_label)

    # Task 2: Implement compute_threshold_prediction
    # Can you write the syntax by urself
    sample1 = {"petal_length":1.4, "species":"setosa", "id":"flower1"}
    prediction = classifier.compute_threshold_prediction(sample1)
    print(f"Prediction:{prediction}") # should print: setosa

    # Task 3: Implement derive_true_label
    sample_setosa = {"species": "setosa", "petal_length": 1.4}
    sample_versicolor = {"species": "versicolor", "petal_length": 4.7}
    # setosa
    print(f"Setosa prediction: {classifier.derive_true_label(sample_setosa)}")
    # not_setosa
    print(
        f"Versicolor prediction: {classifier.derive_true_label(sample_versicolor)}")

    # Task 6: Implement run_prediction_loop
    dataset = setup_application_list()
    correct, wrong, total, y_pred_list = classifier.run_prediction_loop(dataset)

    # Step 5: Calculate accuracy from the returned counters
    # >> Just uncomment the code below, as you have already implemented calculate_accuracy in Task 5.
    accuracy = classifier.calculate_accuracy(correct,total)

    # Step 7: Print a final status message and the summary
    classifier.print_status("Show Summary")
    classifier.print_summary(correct,wrong,total,y_pred_list,accuracy)


if __name__ == "__main__":
    main()
