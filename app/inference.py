from transformers import T5ForConditionalGeneration, pipeline, T5Tokenizer

# Load the fine-tuned model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./fine_tuned_t5_model")
tokenizer = T5Tokenizer.from_pretrained("./fine_tuned_t5_tokenizer")

# Initialize a text generation pipeline
qa_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Example input (nutritional fact)
# input_text = "Is this safe for someone with diabetes? The product contains 320 calories, 12g of fat, 55g of carbohydrates, 3g of fiber, 12g of sugar, and 10g of protein."

# Get the model's prediction
def get_prediction(input_text):
    output = qa_pipeline(input_text)
    return output[0]["generated_text"]

__all__ = ["get_prediction"]