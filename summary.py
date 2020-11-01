from transformers import pipeline

classifier = pipeline("summarization")
results = classifier("Hi are u in the   idiot. Hahhaha ")

print(results)