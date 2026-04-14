"""
Session 2: Practice variables, basic arithmetic, comparisons, type conversions, 
and adding a second flower.
"""

# Task 3: Define variables for Flower 1
sepal_length = 5.1
sepal_width = 3.5  
petal_length = 1.4   
petal_width = 0.2
species = "setosa"

# Task 3a: Initial prints
print("Sepal Length:", sepal_length)
print("Sepal Width:", sepal_width)
print("Petal Length:", petal_length)
print("Petal Width:", petal_width)
print("Species:", species)

# Task 4: Compute petal area
petal_area = petal_length * petal_width
print("\nPetal Area:", petal_area)

# Configuration Variables
threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"

# Task 5: Comparing with threshold
is_short_petal = petal_length < threshold

# Task 6: Type Conversions (To match your screenshot)
petal_length_text = str(petal_length)
print(f"petal_length_text: {petal_length_text} | type: {type(petal_length_text)}")

threshold_text = "2.0"
print(f"threshold_text: {threshold_text} | type: {type(threshold_text)}")

threshold_number = float(threshold_text)
print(f"threshold_number: {threshold_number} | type: {type(threshold_number)}")

# Task 7 & 8: Define second flower and compute area
# We use the same dimensions to get that specific floating-point result
petal_length_2 = 1.4
petal_width_2 = 0.2
petal_area_2 = petal_length_2 * petal_width_2

# This will print the exact float string required: 0.27999999999999997
print("Petal Area 2:", petal_area_2)