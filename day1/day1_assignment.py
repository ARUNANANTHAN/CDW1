# Import necessary libraries
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import nltk

# Download stopwords and WordNet resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stemmer and lemmatizer
ps = PorterStemmer()
wordnet = WordNetLemmatizer()

# Paragraph text for stemming functionality
paragraph = """I have three visions for India. In 3000 years of our history, people from all over
the world have come and invaded us, captured our lands, conquered our minds.
From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
the French, the Dutch, all of them came and looted us, took over what was ours.
Yet we have not done this to any other nation. We have not conquered anyone.
We have not grabbed their land, their culture,
their history and tried to enforce our way of life on them.
Why? Because we respect the freedom of others.That is why my
first vision is that of freedom. I believe that India got its first vision of
this in 1857, when we started the War of Independence. It is this freedom that
we must protect and nurture and build on. If we are not free, no one will respect us.
My second vision for India’s development. For fifty years we have been a developing nation.
It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
Our achievements are being globally recognised today. Yet we lack the self-confidence to
see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
I have a third vision. India must stand up to the world. Because I believe that unless India
stands up to the world, no one will respect us. Only strength respects strength. We must be
strong not only as a military power but also as an economic power. Both must go hand-in-hand.
My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of
space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.
I see four milestones in my career."""

# Example sentences for demonstration
sentences = ['he is a good boy', 'she is a good girl', 'boy & girl are good']

# Step 1: Paragraph Stemming
paragraph_sentences = paragraph.split('.')  # Split into sentences
paragraph_corpus = []

for sentence in paragraph_sentences:
    # Remove non-alphabetical characters
    review = re.sub('[^a-zA-Z]', ' ', sentence)
    review = review.lower()  # Convert to lowercase
    review = review.split()  # Tokenize
    # Remove stopwords and apply stemming
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)  # Join words back into a sentence
    paragraph_corpus.append(review)

# Step 2: Sentence Lemmatization
lemmatization_corpus = []
for sentence in sentences:
    review = re.sub('[^a-zA-Z]', ' ', sentence)  # Remove non-alphabetic characters
    review = review.lower()  # Convert to lowercase
    review = review.split()  # Tokenize
    # Use lemmatization and remove stopwords
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)  # Join back to a single string
    lemmatization_corpus.append(review)

# Step 3: Sentence Stemming
stemming_corpus = []
for sentence in sentences:
    review = re.sub('[^a-zA-Z]', ' ', sentence)  # Remove non-alphabetic characters
    review = review.lower()  # Convert to lowercase
    review = review.split()  # Tokenize
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  # Remove stopwords and stem
    review = ' '.join(review)  # Join back to a single string
    stemming_corpus.append(review)

# Combine all processed corpora
combined_corpus = paragraph_corpus + lemmatization_corpus + stemming_corpus

# Step 4: Creating the Bag of Words model
cv = CountVectorizer(max_features=500, ngram_range=(1, 3))
X = cv.fit_transform(combined_corpus).toarray()

# Output results
print("Vocabulary:", cv.vocabulary_)
print("Bag of Words Matrix:\n", X)