# extractive summarization
# evaluate using ROUGE (Recall Oriented Understudy for Gisting Evaluation)

# ROUGE-L f-score is used for comparing ground truth summary to model summary
# ROUGE-L computes the longest common subsequence b/w two texts. The longer the common subsequence the better it is
# the precision and recall of ROUGE-L will be used.

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np 

import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords 
nltk.download("stopwords")

def tldr(text_to_summarize):
    sentence_tokens = np.array(sent_tokenize(text_to_summarize))
    stop_word_set = list(set(stopwords.words("english")))

    tf_idf_vectorizer = TfidfVectorizer(stop_words=stop_word_set)
    tf_idf = tf_idf_vectorizer.fit_transform(sentence_tokens) # (num_sentences, num_words_per_sentence) i.e, so no word vectors

    sentence_tf_idf_sums_matrix = tf_idf.sum(axis=1) # (num_sentences, 1)
    sentence_tf_idf_sums_array = np.asarray(sentence_tf_idf_sums_matrix).squeeze() # (num_sentences,)

    selected_sentence_indices = np.where(sentence_tf_idf_sums_array > 3)

    summary_sentences = sentence_tokens[selected_sentence_indices]

    summary = "".join(summary_sentences)
    return summary






    

if __name__ == "__main__":
    text_to_summarize = "Hi I am Akash and I am an aspiring Research Engineer. I love to solve complex problems at scale using AI"
