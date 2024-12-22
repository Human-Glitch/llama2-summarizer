import json
import csv

# Function to convert JSONL to CSV for fine-tuning
def jsonl_to_csv_finetuning(jsonl_file, csv_file):
    with open(jsonl_file, 'r') as jsonl_f, open(csv_file, 'w', newline='') as csv_f:
        # Initialize CSV writer
        csv_writer = csv.writer(csv_f)
        
        # Write header row
        csv_writer.writerow(["prompt", "completion"])
        
        for line in jsonl_f:
            # Parse the JSON object from each line
            json_obj = json.loads(line.strip())
            
            # Extract the user's query and context, and the assistant's response
            messages = json_obj.get("messages", [])
            
            # Extracting user prompt (question + context)
            user_message = next((msg for msg in messages if msg["role"] == "user"), None)
            if user_message:
                prompt = user_message["content"].strip()
            else:
                prompt = ""
            
            # Extracting assistant's answer (response)
            assistant_message = next((msg for msg in messages if msg["role"] == "assistant"), None)
            if assistant_message:
                completion = assistant_message["content"].strip()
            else:
                completion = ""
            
            # Write the prompt-completion pair to the CSV
            csv_writer.writerow([prompt, completion])

# Example usage
jsonl_to_csv_finetuning('data/100_train.jsonl', 'data/100_train.csv')