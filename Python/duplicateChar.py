def remove_duplicate(text):
    seen=set()
    result=[]

    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return "".join(result)

def main():
    print(remove_duplicate("farhan hassan"))

main()