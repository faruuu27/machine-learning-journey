def wordFreqCount(sentence):
    words=sentence.split()
    freq={}

    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    return freq

def main():

    text=" farhan hassan uttumadathil jasna afsal afsal ali uttumdathil eshan afsal"
    print(wordFreqCount(text))

main()