#Another task under the text classification umbrella is Question Natural Language Inference, or QNLI. This checks if a premise contains enough information to answer a posed question, determining whether the answer can be found in the given text.

# Create the pipeline
classifier = pipeline (task="text-classification", model="cross-encoder/qnli-electra-base")

# Predict the output
output = classifier("Where is the capital of France?, Brittany is known for its stunning coastline.")

print(output)