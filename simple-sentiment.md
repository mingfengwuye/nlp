# A simple nlp sentiment process 
[Download  sentiment dictionary](http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010)

`//Sentiment dict`

`sentiment_dictionary = {}`

`for line in open('data/AFINN-111.txt')`

    `word, score = line.split('\t')`
    
    `sentiment_dictionary[word] = int(score)`
    
``

`//Get sentimental score`

`total_score = sum(sentiment_dictionary.get(word, 0) for word in words)`
