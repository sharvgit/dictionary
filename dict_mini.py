dictionary_1={}
while True:
    print("\nDictionary managemet System")
    print("1. Add a word")
    print("2. search for meaning")
    print("3.Display all words")
    print("4.update meaning")
    print("5.Delete word")
    print("6.Exit")

    choice=int(input("enter your choice"))
    if choice==1:
        word=input("enter the word").lower()
        meaning=input("enter the meaning")
        dictionary_1[word]=meaning
        print("words suceesfully executed")
    elif choice==2:
        word=input("enter a word to search a meaning:")
        if word in dictionary_1:
            print(f"{word} found in dictionary")
        else:
            print(f"{word} not found in dictionary")
    # elif choice==3:
    #     all_items=dictionary_1.items()
    #     words_all=dict(all_items)
    #     print(f"all elements in the dictionaty are {words_all}")
    # elif choice==4:
    #     example_1={}
    #     print(dictionary_1)
    # elif choice==5:
    #     dictionary_1.pop("brunch")
    #     print("one word is deleted")
    # elif choice==6:
    #     print("exit from the code") 
    #     exit()   
            

    
        

                  


