import nltk
import streamlit as st

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Load the text file and preprocess the data
with open('C:/Users/Bchini.Mahdi/Desktop/Chatbot_Prject.docx', 'r', encoding="ISO-8859-1") as f:
    data = f.read().replace('\n', ' ')

# Tokenize the text into sentences
sentences = sent_tokenize(data)


# Define a function to preprocess each sentence
def preprocess(sentence) -> list:
    words = word_tokenize(sentence)
    words = [word.lower() for word in words if
             word.lower() not in stopwords.words('english') and word not in string.punctuation]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words


# Preprocess each sentence in the text
corpus = [preprocess(sentence) for sentence in sentences]


# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query):
    query = preprocess(query)
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence


def chatbot(question):
    most_relevant_sentence = get_most_relevant_sentence(question)
    return most_relevant_sentence


def main():
    st.title("Chatbot")
    st.write("Hello! I'm a chatbot. Ask me anything about the topic in the text file.")

    # Get the user's question
    question = st.text_input("You:")

    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        st.write("Chatbot: " + response)


if __name__ == "__main__":
    main()

    # New query: "the world is beautiful"
    new_query = "the world is beautiful"
    response = chatbot(new_query)
    st.write("Chatbot: " + response)
