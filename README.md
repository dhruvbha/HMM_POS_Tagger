# HMM_POS_Tagger
Hidden Markov Model part-of-speech tagger for Catalan.
hmmlearn.py will learn a hidden Markov model from the training data, and hmmdecode.py will use the model to tag new data.
> python hmmlearn.py /path/to/input

The argument is a single file containing the training data; the program will learn a hidden Markov model, and write the model parameters to a file called hmmmodel.txt. The format of the model is up to you, but it should contain sufficient information for hmmdecode.py to successfully tag new data.

The tagging program will be invoked in the following way:

> python hmmdecode.py /path/to/input

The argument is a single file containing the test data; the program will read the parameters of a hidden Markov model from the file hmmmodel.txt, tag each word in the test data, and write the results to a text file called hmmoutput.txt in the same format as the training data.

Training data contains - 

A file with tagged training data in the word/TAG format, with words separated by spaces and each sentence on a new line.
A file with untagged development data, with words separated by spaces and each sentence on a new line.
A file with tagged development data in the word/TAG format, with words separated by spaces and each sentence on a new line, to serve as an answer key.
A license and readme files
