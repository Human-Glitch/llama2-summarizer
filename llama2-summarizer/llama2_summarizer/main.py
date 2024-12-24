import replicate
from dotenv import load_dotenv

load_dotenv()

# Define the base model version to fine-tune
BASE_MODEL_VERSION = "meta/llama-2-7b-chat:f1d50bb24186c52daae319ca8366e53debdaa9e0ae7ff976e918df752732ccc4"

# Define the dataset (JSONL file must be publicly accessible)
DATASET_URL = "https://gist.githubusercontent.com/Human-Glitch/c227ba332496f0c827afbde231d7e8a6/raw/4e8093450237557e56e7cfbc197ccf06c3cf6487/samsum_converted_formatted.jsonl"

# Define training parameters
TRAINING_PARAMETERS = {
    "train_data": DATASET_URL,  # Path to your public JSONL dataset
    "num_train_epochs": 3,      # Number of training epochs
    "logging_level": "verbose"  # Set logging level to verbose for detailed logs
}

# Specify the destination for your fine-tuned model
MODEL_DESTINATION = "human-glitch/oss-llm-2"

# Start the training job
# training = replicate.trainings.create(
#     version=BASE_MODEL_VERSION,
#     input=TRAINING_PARAMETERS,
#     destination=MODEL_DESTINATION
# )
 
# print(training)

prompt = "Summarize the following text: 'The quick brown fox jumps over the lazy dog.'"

output = replicate.run(
    "human-glitch/oss-llm-2:281253f13bed359baa0559337330212f846cd2c6912c0874d451d3fcc4b546cf",
    input={
        "debug": False,
        "top_k": -1,
        "top_p": 0.95,
        "temperature": 0.7,
        "system_prompt": "You are a helpful, respectful and honest assistant.",
        "max_new_tokens": 128,
        "min_new_tokens": -1,
        "repetition_penalty": 1.15,
        "prompt": prompt
    }
)

# # The human-glitch/oss-llm-2 model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    print(item, end="")