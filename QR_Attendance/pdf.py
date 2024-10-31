# Query: 
# ContextLines: 1

# Adding more questions for other chapters and expanding content for a full set of 30 questions

questions_answers = [
    ("Chapter 1: Introduction to NLP", [
        ("Q1: What is NLP? Explain its components.", 
         escape_text("NLP (Natural Language Processing) enables machines to understand, interpret, and respond to human language. Its components include: Text Preprocessing, Morphological Analysis, Syntactic Analysis, Semantic Analysis, and Pragmatics.")),
        ("Q2: What is tokenization?", 
         escape_text("Tokenization is the process of breaking down text into smaller units called tokens (words, phrases, or symbols) for easier analysis in NLP tasks like machine translation and text classification.")),
        ("Q3: What is the minimum edit distance?", 
         escape_text("It is the minimum number of operations (insertion, deletion, substitution) needed to convert one word into another. It’s used in spell checkers and text comparison.")),
        ("Q4: Define ambiguity in NLP. What are the types of ambiguity?", 
         escape_text("Ambiguity occurs when a sentence can have more than one interpretation. Types include lexical ambiguity (word meaning) and syntactic ambiguity (sentence structure)."))
    ]),
    
    ("Chapter 2: N-Gram Language Model", [
        ("Q5: Explain the concept of perplexity in N-Gram models.", 
         escape_text("Perplexity measures how well a language model predicts a test set. A lower perplexity indicates a better model.")),
        ("Q6: What is Laplace smoothing in N-Gram models?", 
         escape_text("Laplace smoothing adds a small constant to N-Gram counts to handle zero-probability problems, ensuring every word sequence has a non-zero probability.")),
        ("Q7: What are Kneser-Ney and Good-Turing smoothing techniques?", 
         escape_text("Good-Turing estimates the probability of unseen events. Kneser-Ney adjusts probabilities based on how commonly a word appears in different contexts.")),
        ("Q8: What are the limitations of N-Gram models?", 
         escape_text("N-Gram models have limitations such as ignoring long-term dependencies and context beyond the N-sized window. They also suffer from data sparsity issues."))
    ]),
    
    ("Chapter 3: Text Representation", [
        ("Q9: Explain the Bag-of-Words (BoW) model.", 
         escape_text("BoW represents text as an unordered collection of words where each word's occurrence is counted, ignoring grammar and word order.")),
        ("Q10: What is the difference between Word2Vec and GloVe embeddings?", 
         escape_text("Word2Vec is neural-based predicting word context. GloVe is a matrix factorization method using word co-occurrence statistics.")),
        ("Q11: What does TF/IDF represent?", 
         escape_text("TF measures word frequency in a document, while IDF reduces the weight of common words across documents.")),
        ("Q12: What is the curse of dimensionality in text representation?", 
         escape_text("The curse of dimensionality refers to the difficulty of processing high-dimensional data, leading to inefficiencies and sparsity in models."))
    ]),
    
    ("Chapter 4: Syntax and Parsing", [
        ("Q13: What is the difference between dependency and constituency parsing?", 
         escape_text("Dependency parsing focuses on the relationships between words, while constituency parsing focuses on dividing a sentence into subphrases based on grammatical structure.")),
        ("Q14: What are context-free grammars?", 
         escape_text("Context-free grammars are a set of recursive rules used to generate patterns of strings, commonly applied in syntax analysis.")),
        ("Q15: Explain CKY algorithm in parsing.", 
         escape_text("The CKY algorithm is a dynamic programming parsing technique used for context-free grammars. It constructs parse trees by breaking sentences into smaller parts.")),
        ("Q16: What are POS (Part of Speech) tags?", 
         escape_text("POS tags assign grammatical categories to words in a sentence, such as nouns, verbs, and adjectives, aiding in syntactic analysis.")),
    ]),
    
    ("Chapter 5: Semantic Analysis", [
        ("Q17: What is word sense disambiguation?", 
         escape_text("Word sense disambiguation is the process of determining which meaning of a word is being used in a particular context.")),
        ("Q18: What is semantic role labeling?", 
         escape_text("Semantic role labeling assigns roles to words or phrases in a sentence, such as agent, patient, and action, to capture the meaning of the sentence.")),
        ("Q19: Define Named Entity Recognition (NER).", 
         escape_text("NER is the process of identifying and classifying entities in a text into predefined categories such as person names, organizations, and locations.")),
        ("Q20: Explain the difference between polysemy and homonymy.", 
         escape_text("Polysemy refers to a single word having multiple related meanings. Homonymy occurs when two different words share the same spelling or pronunciation but have unrelated meanings."))
    ]),
    
    ("Chapter 6: Machine Translation", [
        ("Q21: What is the difference between rule-based and statistical machine translation?", 
         escape_text("Rule-based translation relies on linguistic rules and bilingual dictionaries, while statistical translation learns translations from large amounts of parallel text data.")),
        ("Q22: Explain the BLEU score in machine translation.", 
         escape_text("The BLEU score measures the quality of machine-translated text by comparing it to a human reference translation. Higher scores indicate better translation quality.")),
        ("Q23: What are phrase-based translation models?", 
         escape_text("Phrase-based models break down sentences into phrases for translation rather than individual words, capturing context better and improving accuracy.")),
        ("Q24: Describe neural machine translation (NMT).", 
         escape_text("NMT uses neural networks, particularly sequence-to-sequence models, to translate text. It improves over statistical methods by handling longer dependencies and producing more fluent translations."))
    ]),
    
    ("Chapter 7: Speech Recognition", [
        ("Q25: What is acoustic modeling in speech recognition?", 
         escape_text("Acoustic modeling represents the relationship between linguistic units and audio signals in speech recognition systems.")),
        ("Q26: Explain the role of language models in speech recognition.", 
         escape_text("Language models predict the probability of word sequences, helping to improve accuracy by ensuring that recognized speech follows grammatical rules.")),
        ("Q27: What is the Hidden Markov Model (HMM)?", 
         escape_text("HMM is a statistical model used to represent the sequence of observable events (like audio signals) and their hidden states, frequently applied in speech recognition.")),
        ("Q28: What is the difference between speech-to-text and text-to-speech systems?", 
         escape_text("Speech-to-text systems convert spoken language into written text, while text-to-speech systems synthesize speech from written text."))
    ]),
    
    ("Chapter 8: Sentiment Analysis", [
        ("Q29: What is sentiment analysis?", 
         escape_text("Sentiment analysis identifies and categorizes opinions expressed in a text, determining whether the sentiment is positive, negative, or neutral.")),
        ("Q30: Explain the difference between rule-based and machine learning approaches in sentiment analysis.", 
         escape_text("Rule-based approaches rely on predefined sentiment lexicons and rules. Machine learning approaches use labeled datasets to train classifiers, which can learn more nuanced sentiment patterns.")),
        ("Q31: What are challenges in sentiment analysis?", 
         escape_text("Challenges include handling sarcasm, negation, and domain-specific language, which make it difficult to accurately detect sentiment in text.")),
        ("Q32: What is aspect-based sentiment analysis?", 
         escape_text("Aspect-based sentiment analysis identifies specific aspects or features of an entity in text and determines the sentiment expressed towards them."))
    ])
]

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Important NLP Exam Questions and Answers", ln=True, align='C')

# Set font for content
pdf.set_font("Arial", size=12)

# Write content to PDF
for chapter, qas in questions_answers:
    # Add chapter title
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=chapter, ln=True)
    
    # Add questions and answers
    pdf.set_font("Arial", size=12)
    for q, a in qas:
        pdf.multi_cell(0, 10, txt=f"{q}\nAnswer: {a}\n")

# Save the PDF
output_path = "/mnt/data/NLP_Exam_Questions_Answers_Updated.pdf"
pdf.output(output_path)

output_path
