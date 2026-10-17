def freq_Count(text):

    freq={}

    for ch in text:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    return freq

def main():
    text="farhan"
    print(freq_Count(text))

main()