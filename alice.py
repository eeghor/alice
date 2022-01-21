import requests
from string import punctuation
from collections import defaultdict, Counter

class WordMapper:

    def __init__(self):

        # taken from spacy 3.2.0
        STOPWORDS = {"'d", "'ll", "'m", "'re", "'s", "'ve", 'a', 'about', 'above','across', 'after',
                     'afterwards', 'again','against', 'all', 'almost', 'alone', 'along', 'already', 'also', 
                     'although', 'always', 'am', 'among', 'amongst', 'amount', 'an', 'and', 'another', 'any', 
                     'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 
                     'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 
                     'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'bottom', 'but', 
                     'by', 'ca', 'call', 'can', 'cannot', 'could', 'did', 'do', 'does', 'doing', 'done', 'down', 
                     'due', 'during', 'each', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 
                     'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 
                     'fifty', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'four', 'from', 'front', 'full', 
                     'further', 'get', 'give', 'go', 'had', 'has', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 
                     'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 
                     'hundred', 'i', 'if', 'in', 'indeed', 'into', 'is', 'it', 'its', 'itself', 'just', 'keep', 'last', 
                     'latter', 'latterly', 'least', 'less', 'made', 'make', 'many', 'may', 'me', 'meanwhile', 'might', 
                     'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', "n't", 'name', 
                     'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 
                     'not', 'nothing', 'now', 'nowhere', 'n‘t', 'n’t', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 
                     'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 
                     'per', 'perhaps', 'please', 'put', 'quite', 'rather', 're', 'really', 'regarding', 'same', 'say', 'see', 
                     'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 
                     'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 
                     'still', 'such', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 
                     'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'third', 'this', 
                     'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 
                     'toward', 'towards', 'twelve', 'twenty', 'two', 'under', 'unless', 'until', 'up', 'upon', 'us', 'used', 
                     'using', 'various', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 
                     'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 
                     'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 
                     'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', '‘d', '‘ll', '‘m', '‘re', 
                     '‘s', '‘ve', '’d', '’ll', '’m', '’re', '’s', '’ve'}

 someficujj24rgr = defaultdict(int)

def get_alice():
    
    start_reading = False
    
    for line in requests.get('https://www.gutenberg.org/cache/epub/28885/pg28885.txt').text.split('\n'):
        
        if 'CHAPTER I' in line:
            start_reading = True
        elif 'THE END' in line:
            start_reading = False
            
        if start_reading:
            if ('[' not in line) and ('*' not in line):
                yield ''.join([ch for ch in line if ch not in punctuation])

def get_other_text():

    other_text = []
    
    with open('/Users/ik/Codes/alice/data/textos.txt')as f:
        for line in f.readlines():
            if stripped_line := line.strip():
                other_text.append(stripped_line)

    return other_text


alice_text = '\n'.join([line for line in get_alice()])
other_text = get_other_text()

text_word_count = Counter(word for line in other_text for word in line.split()).most_common()
alice_word_count = Counter(word for line in alice_text for word in line.split()).most_common()

print(text_word_count)