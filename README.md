# Similarity Analysis using SpaCy

This code demonstrates how to use the SpaCy library to calculate the similarity between words and sentences.

## Prerequisites

To run this code, you need to have the SpaCy library installed, as well as the 'en_core_web_md' model.

## Installation

1. Install Docker
2. Clone the repository
3. Build the Docker image by running the following command in the repository directory:

> docker build -t nlp-similarity-sentences .

4. Run the Docker container by running the following command:

> docker run -p 80:80 gardenpath-sentences

5. Or you can just run the code from the terminal once you've cloned it.




## Description

The code begins by loading the 'en_core_web_md' model from the SpaCy library. It then defines six words: "cat", 
"monkey", "banana", "judo", "boxing", and "climbing", and calculates the similarity between them using the similarity() 
method.

The code then creates a sentence consisting of the words "cat", "apple", "monkey", and "banana", and calculates the 
similarity between each pair of words.

Finally, the code compares a given sentence ("Why is my cat on the car") to a list of other sentences and calculates 
the similarity between them.

## Results

The code outputs the similarity scores between various pairs of words and sentences. It's interesting to note that the 
library is able to find similarities across groups such as animals and fruits, and that there are greater similarities 
within groups than across groups.

The code also introduces three new words: "judo", "boxing", and "climbing", and demonstrates how the library is able to 
determine the similarities between them.

## Example results

> judo boxing
> 0.9999999706076033
> 
> climbing monkey
> 0.2253446640572971
> 
> climbing cat
> 0.07278902163657651