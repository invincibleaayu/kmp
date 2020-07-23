#yesma django ma integrate garda savai lai to lower ma lag hai for optimin result

def compute_prefix_function(pattern):
    count=0
    length=len(pattern)                                            #text length
    array_of_prefix_function=[0 for _ in range(length)]         #creating list of length of text
    pattern_list=list(pattern)
    i,j=0,1

    while i < length and j < length:
        if pattern_list[i]==pattern_list[j]:                          #case 1 yesma chai aagadi rah paxadi ko milni wala
            array_of_prefix_function[j]=i+1
            i+=1
            j+=1
            
        else:
            if i==0:                                           #case 2 yesma chai initial case ani match nahuda
                array_of_prefix_function[j]=0                   #aagadi array sarni wala herxa hai 
                j+=1
            else:
                i=array_of_prefix_function[i-1]                #case 3 array lai aagadi sarni kaam garxa
    return(array_of_prefix_function)

def KMP_matcher():
    matched_character_no = 0
    text="abxabcabcabyabcababcaby"
    text=text.replace(" ","")
    text=list(text)                                                   #conversion of string to list
    pattern=input("Please enter a text:")
    pattern=pattern.replace(" ","")                                   #removes space from the input string
    pattern=list(pattern)                                             #conversion of string to list
    array_of_prefix_function=compute_prefix_function(pattern)
    length_of_text=len(text)
    length_of_pattern=len(pattern)
    print(array_of_prefix_function)

    #now we check and search for the string to be matched
    for i in range(0,length_of_text):

        while matched_character_no > 0 and  pattern[matched_character_no] != text[i]:
            print("inside while")
            matched_character_no=array_of_prefix_function[matched_character_no]

        if pattern[matched_character_no] == text[i]:
            print("inside if",matched_character_no)
            matched_character_no+=1
            
            
        elif matched_character_no==length_of_pattern:
            print("pattern occurs with shift {}".format(i))
            matched_character_no = array_of_prefix_function[matched_character_no]



    


KMP_matcher()



