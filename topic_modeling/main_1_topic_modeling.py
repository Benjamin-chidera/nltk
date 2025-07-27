import spacy

nlp = spacy.load("en_core_web_sm")

# documents = [
#        "The football game ended with a surprising score and team victory.",
#        "The basketball championship drew millions of fans as the final game went into overtime."
#        "The soccer game was a disappointment for both teams.",
#        "The hockey game ended with a 1-1 tie and a 2-0 win for the visitors.",

# ]

documents = [
    "The election results sparked debates about voting systems and policies.",
    "AI and machine learning are transforming the tech industry rapidly.",
    "The football game ended with a surprising score and team victory.",
    "Stock market trends indicate a rise in technology investments.",
    "Vaccines and public health policies are critical for disease prevention."
]

def process_doc(text: list):
    processed_text = []
    
    for doc in nlp.pipe(text, disable=["parser", "ner"]):
        tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
        
        processed_text.append(tokens)
    return processed_text        
        
processed_doc = process_doc(documents)
# print("Processing Documents: ", processed_doc)

processed_doc = [" ".join(doc) for doc in processed_doc]

# print("Processed Documents: ", processed_doc)
