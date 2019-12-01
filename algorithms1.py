
def prelims_info():
     print("Dataset: vibrio_cholerae")
     

'''method serves to read from text file where argument is file name'''
def read_text(file_name):
     contents = ""
     f=open(file_name, "r")
     if f.mode == 'r':
          contents =f.read()
     return contents


'''counts how many times a pattern appears in a given DNA sequence'''
def PatternCount(Text, Pattern):
     
     count=0
     for i in range(0,len(Text)-len(Pattern)+1):
          if Text[i:i+len(Pattern)]==Pattern:
               count=count+1
     return count

def FrequentWords(Text,k):
    frequent_patterns = {}
    for i in range(0,len(Text)-k):
        pattern = Text[i:i+k]
        count = PatternCount(Text,pattern)
        frequent_patterns.update({pattern:count})
    highest=max(frequent_patterns.values())
    result=([k for k, v in frequent_patterns.items() if v == highest])

    return result   

def ReverseComplement(pattern):
    complements_dictionary = {'A':'T','C':'G','T':'A','G':'C'}
    reverse_complement = ""
    
    for i in range(len(pattern)):
        reverse_complement =reverse_complement+ complements_dictionary[pattern[i]]
    
    return reverse_complement[::-1]
    

def PatternMatching(Pattern,Genome):
    count =[]
    for i in range(len(Genome)):
        if Pattern == Genome[i:i+len(Pattern)]:
            count.append(i)
    return count

def ClumpFinding(s, k, L, t):
    out = []
    for start in range(len(s)-L+1):
        window = s[start:start+L]
        counts = {}
        for i in range(len(window)-k+1):
            if window[i:i+k] not in counts:
                counts[window[i:i+k]] = 0
            counts[window[i:i+k]] += 1
        for kmer in counts:
            if counts[kmer] >= t and kmer not in out:
                out.append(kmer)
    return out


#print(FrequentWords("TTGACATCGTAAATTGTCTCATTCATTTTAAATTGTCTAAATTGTCACCTGCCCTTAGACTTGTAGAGACTTGTAGTAAATTGTCACCTGCCCTTACCTGCCCTTTAAATTGTCTTGACATCGTTGACATCGTCATTCATTTTAAATTGTCTAAATTGTCTAAATTGTCACCTGCCCTTTAAATTGTCACCTGCCCTTTAAATTGTCACCTGCCCTTACCTGCCCTTTTGACATCGACCTGCCCTTACCTGCCCTTTAAATTGTCTAAATTGTCAGACTTGTAGTCATTCATTTACCTGCCCTTACCTGCCCTTACCTGCCCTTACCTGCCCTTTAAATTGTCACCTGCCCTTAGACTTGTAGAGACTTGTAGAGACTTGTAGAGACTTGTAGAGACTTGTAGACCTGCCCTTTAAATTGTCACCTGCCCTTTCATTCATTTTTGACATCGAGACTTGTAGTAAATTGTCTCATTCATTTTCATTCATTTACCTGCCCTTAGACTTGTAGTTGACATCGAGACTTGTAGAGACTTGTAGTAAATTGTCACCTGCCCTTTTGACATCGTCATTCATTTACCTGCCCTTAGACTTGTAGTCATTCATTTTTGACATCGTAAATTGTCTTGACATCGTCATTCATTTTCATTCATTTTAAATTGTCACCTGCCCTTACCTGCCCTTAGACTTGTAGTCATTCATTTTTGACATCGTCATTCATTTTCATTCATTTTTGACATCGTCATTCATTTACCTGCCCTTTAAATTGTCTCATTCATTTACCTGCCCTTTAAATTGTCTCATTCATTTTTGACATCGACCTGCCCTTTAAATTGTCAGACTTGTAGTCATTCATTTTAAATTGTCTAAATTGTCAGACTTGTAGACCTGCCCTTTCATTCATTT",11))
#prelims_info()
#text = read_text("vc.txt")
#count = PatternCount(text,"GCG")
print(ClumpFinding("ATGATCTCGAGATCTGATTCTGCAGCCGAACCTTCCGTATACCGGGGACCCCCGTGCCGACGCATTGGTCGTGGTTCACCTCGCGGCCATGCAGACTAAGCTGTAAATCCAGGTAGCGAAACCTGGTGTACGCTTATGGTGGGGAGGCTCCTATAACAGTGACCGCTAGGCCCGTTATTTTTGTCCGTCTGGTTCCTAGGGGCGTGTAGCTGGCTGCCAATCCCGGCCTAGTTCCCTGGACCACGAGTTTAAAGGCCGGGGGTGGGCCGGGGGTGGGGGTGGTATGAGACAACCTGCCATAGCACCACCTATTTCTACGGGTGAAAGTTGCGCGGTGAACTCCATAATGCCGACAGAGTGGACAATCATTTCCAATGTGGGTTTTCTGGGGTGTATTCCGGGTTTTGACCTCACGGGCACGAGGGGTTGGGAGCACCGCACGGCGTCAGTTTCTTACCAATGGCACGAGACCTAATCACCTACTATATATTGGCAAGCCAATCGCGGGCGGCTTGAACTCTCATCTCATCCCTCCATAGTGCTTCACCAATGTTAAGGGATGGGATGGATGGGATGATACTACGTAGCACGCCTAGATCGGATAGTTCAGATAAATCGTCGGCAACGTCAACGCCGGAAACTAAAATGAGACGAGGAAGTGATGGACTAGTGATTCTACCTTAGATTCGGTTACGTCTCGGTTAACCGGAGGGAGCGAGACACACACTGGCGAACGAAATAATGTCTTGAGAAAACCGAGCGGATACAGGAATAGTCTGGGGAAATTGAAGATGCGGGGACCCACGCTGAAAAAACCGGAAACCCCCCCGTGATCTCGATCCCGGAATGGTGCCAATATCATGTACTGCGGTAGAGTGAGGACTATCGTAAGCTACATATACCAAGTTGGAGCTTTTGGTTAGGAAAAATGTGAGCGGCCTCCGGGGGGTCCGGGGTTCTGTCAAAGTGTCGTCAAACTTATTAAGCTATGGACAAGTGCGGACTGATCGGGTCTGGCGGGCGGGAGTGTAGGTGATTTCCGTAAGGAATGGCAATACCGGGAAAGCATTGATGTGCGTATCTGAGGGATTACACTCTTCGATGCTGTGCCCCATAAGCCGGCGCCGAGCAGATCGGGTTGATAGCTCCGCCGAGTTGATTAGTACCATTGGGGAAGTGCGTTCAAGTTGACAATCCCGGAGACTTAGAGCCCGCCCTCCCTGTAGTAGCCGCAAGACTTGAATGCCCGTAATAGGTTAAGATTTCCGCTTTGCAAAGAGACGAACTAGGTTCAGGCAAATCTTGGTTATAGAAAAGTCCGCGGTTTGGTAGCCACTACGCGTGAAGCATGATCGTAGGCCTCCCTTATGCTTAGGCCATCCGCGTAGGATACTCTTCGTCCGCCTATAAAGTATGTTAGTGGTTACCTGTAAAGTTAGTCAGTAGCCAACGCCGCTATTTGGTTGGTTTCCTCGATAGACGCATGGGCGAGAATACACACGCATGATGGAGGGCGACCGACGAGAGTCGACGAGAGTGTGTTATGTGTATGTATAGATGACAGACATTCCGAGTTGGACCCCTAAGATGCGTCCGGGAAAATGATGGGTATGGTATTGATGGGTATAGACCCGAAAATCGGCACGCCGCTACAACCCGGCCGTACCCTTCATGTTAGGTGCTGCGTTTATTCTTAATAGCCAGCGATGGCTTAGTGTAATGCCCCTGCAGATCTCGTGACTTTCCACGTCTCTCGTAGAAATCCGGGATCTCTCCCAGCGCCTTAAGATGAGCAGACATGTAGTTTGGTAGATGGTGGGATCTAGCTAAAGTAGGTGACGCTGGAGGGATCAGAATTATGGCTGATTCCGGGCAAATCAGTCCCGGACCCCGGATTGAAACCTAGGAAGCTGGCAGCACTCTTCATTCACGAATTCACGACTCGTGATGTACTCTCGTGATGTATGT",5,100,4))
#Genome="GGGCGCGGGGCGCGAAGCTATGGGCGCGAATTTCAAGGGCGCGGGGGCGCGCTGGGCGCGCGCGGGCGCGGTGGCAATTGGGCGCGTGTGGGGGCGCGCGGGCGCGGGGCGCGAGGGGGCGCGGCCGATGGGGACGGGCGCGGGGCGCGCAAATTGGGCGCGCATTGGGCGCGAGGGCGCGAGGGGCGCGTCGGGCGCGTGGGCGCGAAGGGCGCGTCTCCCCGGGCGCGCCGAGGGCGCGGTGGAGGGGTCCGGGCGCGAGGGCGCGGGCGACGCGGGCGCGCCGGGCGCGCTGGGCGCGGCCGCTCTGGGCGCGCGGGCGCGACGGGCGCGTCTTGGGCGCGCTTTACCGGGCGCGAGAGGGCGCGGGGCGCGGGGCGCGCGGGCGCGTAGGGCGCGTCCGGGCGCGCTGGGCGCGGCTTAGGGGCGCGCCGACGGGCGCGCGAGGGGCGCGGGGCGCGCAGGGGCGCGCCGGGCGCGGGGGGCGCGGGGGCGCGGGGCGCGGGGCGCGCGGGCGCGTGGGCGCGAGGGGCGCGGGGCGCGTCTGCCTGGGCGCGGTAGAGCCGGGCGCGGGGCGCGCGCCTGAAAGGGGCGCGAGGACGAAGGGCGCGGGGCGCGATTTGGGCGCGCTCGGGCGCGGGGCGCGCTGGGGGCGCGGGGCGCGTGGGCGCGGGGGCGCGAACAGGGCGCGCGGGCGCGGGGGCGCGGGGCGCGAGGGGGCGCGATGCCTGCGTGGGGCGCGGGGCGCGCCAGGGCGCGAAAGGGCGCGAAGGGCGCGCGGGCGCGCGGGCGCGGGGCGCGATTGGGGCGCGGGGCGCGTGGGCGCGGGGCGCGTTACCGGGGCGCGTTGGGCGCGTGTGGGGCGCGGGCTAGGGCGCGTCCGGGCGCGATTGGGCGCGGGGCGCGGAAAAGGGGCGCGGAGGATATGGGCGCGGGGGCGCGCCGGGCGCGGGAGTTTGGGCGCGTACGACAACGCTTAAGGGCGCGGTGGGGGCGCGAAATGGGCGCGTAGGGCGCGCATTGGGGCGCGGGGGGCGCGCCGGGCGCGCGGGCGCGGCAGGGCGCGTTACTGTGGGCGCGATGGGCGCGGGGCGCGGGGCGCGGGGCGCGCGGGCGCGAAGTGGGCGCGGGGCGCGGTTGGGCGCGGGGGCGCGTGGGCGCGGGGCGCGGAGGGCGCGGGGGCGCGCTAGGGCGCGGGGCGCGTAGGGCGCGCACGGGCGCGGGGCGCGCTTTTCGACGGGCGCGAGGGCGCGCGGGGCGCGCGGGCGCGCGGGCGCGTTGTGCGGGCGCGTAGTGGTTTTAGTGGGCGCGGGGCGCGCGGGCGCGATGGGCGCGGGGCGCGCTTGGGGCGCGACGGGCGCGTGACGGGGCGCGGGGCGCGGGGCGCGGGGCGCGTTGGGCGCGGGGCGCGGGGCGCGGGGCGCGCCTGCAATGTGGGCGCGTCCGTAGGGCGCGCCGGGCGCGGACGGGCGCGGGGTGGGCGCGGTACAGGGCGCGCACGGGCGCGTAGTAAATGGTGGGCGCGGACGGGGCGCGAGGGCGCGAGGGCGCGTGTCAGGGCGCGTGAGGGCGCGTGTAGGGCGCGTGGGCGCGTGGGCGCGTCAGGGGCGCGCGGGCGCGGGGCGCGGGTCGGACGTTGGGCGCGCTCGACGTAGCGGGCGCGAGGGCGCGCATCCGTCGTCTCTGCAGGGCGCGCCGGGCGCGGGGCGCGCAGGGCGCGGGGCGCGACAAGGGCGCGATGGGCGCGGTGGGCGCGGCTGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGAATGCTCTAGGGCGCGGGGGCGCGCTCAACGGGCGCGGGGGCGCGGGGCGCGGAGGGCGCGCGGGCGCGTTGGGCGCGGGGCGCGGTGGGCGCGTGGGGCGCGAGAGCGGGCGCGGGGGCGCGAGGGGCGCGAAGGGCTTCACCAGGGGCGCGTGGAGGGCGCGTCATGGGGCGCGTTGGGCGCGGGGCGCGGAAGGGCGCGCGGGCGCGACGGGGGGCGCGCGGGCGCGGGGGCGCGCAGACACTGGGCGCGATCTTGGGCGCGAGGGCGCGGTCATTTTGTGCGGGCGCGGGGCGCGGTCGGGGCGCGCCTTGGGCGCGAGATTCTGGGCGCGGGGCGCGTATCTTGGGCGCGAGGGCGCGGGGGGCGCGGGGCGCGGGGCGCGCGGGCGCGCATGGGCGCGGGGCGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGCGGGCGCGCAGGGGCGCGATATGAGGGGCGCGGGGCGCGCGGACCGGGCGCGTGGTGGGCGCGGGGGCGCGTACAAGGGCGCGCGGGCGCGGGGCGCGGTGGGGCGCGGGGCGCGGTGGGCGCGGAGTAAAGTGGCGGGCGCGATTGGGCGCGGGGCGCGCTTGGGCGCGGGGCGCGGGGCGCGTTGGGCGCGGGGCGCGGCGCCCAAGAGGGCGCGGATAGGGGGGCGCGGGTTCGAAAAGCTGGGCGCGGGGCGCGGCTGGGCGCGGCGCAAGGGGGCGCGGGGGCGCGCAGGGGCGCGGGGCGCGGGGGGCGCGGGGCGCGACGTGCGCTGTCGGGCGCGAGGGGGCGCGCGGGCGCGCGGGCGCGCGATGTGGGGCGCGAAGCTATGTAATGGGCGCGTGGGCGCGGGGCGCGCACACGGGCGCGTACCGGGCGCGGCCGGGGGCGCGCTTGGGGCGCGACGGGCGCGGGGCGCGCGGGCGCGGGGCGCGGGGCGCGGGGCGCGGCGTGGTGGGGGCGCGGGGCGCGTACTTGGGCGCGCTAAATGGGCGCGCGCAGTTACGGGCGCGGGGGCGCGGGGCGCGTTGGGCGCGTGGGCGCGGGGCGCGGGGCGCGCTATAGGGGCGCGTGGGCGCGGGGCGCGATAGGTTCTTTAGCAGTAGGGCGCGGGGCGCGTTGGGGCGCGTCGGGCGCGAAAGGGCGCGATGGGCGCGCGTATTAATGGGCGCGGGGCGCGGGGGGCGCGGGGCGCGAAGGGCGCGACAGGGCGCGGCGGGCGCGTGGGGCGCGCAGTGTCTCCGGGGCGCGGGGCGCGAGGGGCGCGGGGCGCGTCGCGGGCGCGAGGGGGCGCGAGGGCGCGTGGGCGCGTCGGGCGCGTGCGGGCGCGGGGCGCGTGGGAGGGCGCGCTGTCAGGGCGCGCAACCATAGGGCGCGTAGGGCGCGGGGGCGCGTGGGCGCGCGGGCGCGCGTCAATGGGCGCGGGGCGCGAGGGCGCGCACAGGGCGCGGAGCAGGGCGCGTGGTCTCCGGGCCGGATACGGTGGGGCGCGACGGGCGCGGGGCGCGGGGCGCGAGGGCGCGTGGGCGCGGGGCGCGCTAGGGCGCGAGACTGATAACGAAAAGGGCGCGCTGGGCGCGCTGGGCGCGAACAGCGGGGCGCGGGGCGCGTTCTAGCTGACGGGCGCGACGGGCGCGGGAGCCGGGGCGCGGGGCGCGCGGGCGCGGGGCGCGGGGCGCGTGGGGGCGCGTGGGGCGCGGGGCGCGGGGCGCGTGGGCGCGAGGGCGCGCGGGCGCGGGGCGCGCGGGGCGCGCGGGCGCGGGGCGCGTTTGGGCGCGGGGCGCGCAAACCATGGGCGCGATTCTTACCGTACATGGGCGCGGGGCGCGCCGGGCGGGCGCGGGGCGCGTCAACCGGGCGCGTAGGGCGCGGGGCGCGATTGGGCGCGGGGCGCGGGGCGCGGGGCGCGTATGGGCGCGGGGCGCGGGGCGCGTGCGGGCGCGAAGGGCGCGAGGGCGCGGGGCGCGTGGGCGCGAGGGCGCGGGGCGCGAGGGCGCGGGGCGCGAGAGAATGGGCGCGAATTTGGGGCGCGGAGATTGGGCGCGGCGGGCGCGGTAGGGCGCGGGGCGCGAGGGGCGCGGGACCTGGTGCCGGGCGCGGGGCGCGGGGCGCGGGGCGCGGTGGGCGCGGCGGGCGCGGGGCGCGGGGCGCGTGGGCGCGGAGGGCGCGTAGTGTGGGCGCGAACGTAATTGGGCGCGGAGTACAGGGCGCGGCCGGGCGCGGGGCGCGCTTCCGGGCGCGGGGGCGCGCATGGGGCGCGGGGGCGCGCTTTGGGCGCGGGGCGCGGGGGCGCGGCGGGCGCGCTGGGGCGCGCGGGCGCGCACTCTCTAATCCGGGCGCGGTGGGGGCGCGAGGGCGCGAAAGTGAGGGCGCGGGGGCGCGCGCGAGGGCGCGTGGGCGCGAGGGGCGCGGTGGGCGCGAATGGGGGCGCGCGGGCGCGCCGGGCGCGGGGCGCGGGGCGCGACCGCGGGCGCGGGGGCGCGGGGCGCGACGGGGCGCGGGGCGCGAGGGAATGGGCGCGTATGAAACGTTGGGCGCGAAGGGCGCGTTTCGTAAGGGCGCGGGGCGCGGGGCGCGTTGCGATTCGGGCGCGCTGGGGCGCGGTGTGGGCGCGAAGGGCGCGTGGGGCGCGCGGGCGCGTGGGCGCGCCGGGCGCGCTAGGGCGCGGGGCGCGCGGGCGCGTAGCTGAGAGGGCGCGGGAGGGCGCGCGTCGTGTAGGGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGTACACCCCCCAGGGGCGCGGGGCGCGGGCAGGGCGCGCGGGGCGCGTGGGGGGCGCGGGGCGCGGGGCGCGACCAGGGCGCGCGGGCGCGGGGCGCGGCGCGGGCGCGGGGCGCGCTGGGCGCGGGGCGCGAATCGGGCGCGGGGCGCGCGGGGCGCGAGAGCCGGGCGCGTGGGCGCGGGAAGGGGGCGCGGGGCGCGGATGGGCGCGTGGATTGGGCGCGTGGATTCCCTGCAACGGGGCGCGACGAGCCCACCTGGGCGCGGGGCGCGTGGGCGCGGGGCGCGCCCGGGCGCGGTGGGCGCGGGATTCTAGGGCGCGAAGGGCGCGCGTAGGGCGCGGTCGCGGGGCGCGTAGCCGTCACGGGCGCGCTAGAAGGGCGCGGGGCGCGTGGTGGGCGCGGGGCGCGTTGGGCGCGTGGGGCGCGGTGGGCGCGTGCGGGGCGCGGGGGCGCGCCGGAGGATGGGCGCGGGGCGCGCCTACCAAGGGGCGCGGAGGGCGCGGTCGGGCGCGTAACGGAAAGGGCGCGCGACTTGTGGGCGCGCGGGCGCGAAGGGCGCGTCAGGGCGCGCTCTGCGGGCGCGCGGGCGCGATGCCGCGGGCGCGTCCTGGGCGCGGGGCGCGTGGGCGCGATCGGGCGCGCTGGGGCGCGTGGGCGCGTAGGGGCGCGGGGCGCGGGGCGCGGTAGGGCGCGCGGCCGGGCGCGGGGCGCGTGGGCGCGAGGGCGCGAGGGCGCGGGGGCGCGGTAAGGGCGCGGGGCGCGAAAAGGGCGCGGTGGGCGCGTGGGCGCGCAAACTTACGCTGGGGCGCGGGGGCGCGGCTTGGGCGCGTCGGGCGCGGGGCGCGGAGGGCGCGGTCAGGGGCGCGAGGGCGCGTGGCGGGCGCGCGGGCGCGAGGGCGCGATCGGGCGCGCGGGCGCGCTAGGGCGCGGGGCGCGTGGGCGCGGGGCGCGGGGCGCGCGTATGGGCGCGAATTACGGGGCGCGGGTGGGCGCGTAAGGGCGCGTTGGGCGCGTTGGGCGCGGGGCGCGGGGGCGCGGGGCGCGGGGGCGCGCGGGGCGCGCACGTAGCGGGCGCGGGGCGCGCAAGGGGCGCGTCCTGGGCGCGTAGGGGGCGCGTGTGGGCGCGCCGGGGGGCGCGGGGCGCGCGGGCGCGGGGCGCGTGGGCGCGCCAGGGCGCGCCGGGGCGCGGGGCGCGGGGCGCGGTGGGCGCGTGTGGGCGCGGGGCGCGCTGGGCGCGGGGCGCGCGAACGTAACTGGGCGCGTCACGGGGCGCGATAGGGCGCGGGGGCGCGAGGGCGCGTGGGGCGCGCGGCCGGGCGCGCCTGGGCGCGTGGGCGCGCGGGGCGCGCAGGGCGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGCCGTGGGCGCGAAGGGCGCGGGGCGCGGGGCGCGCACATGGGGCGCGTCCGCCTGGGGCGCGGGGCGCGCCGGGCGCGGCGGGCGCGCCTTAAGGGCGCGGTTGATTGGGCGCGCGGGCGCGTCGGGCGCGTGGGCGCGGGGCGCGAGTAAGACGGGCGCGAATGGATGGGCGCGGGGCGCGATGGGGCGCGTGGGCGCGTGGGCGCGGGGCGCGCGTTCGGGCGCGCCACTGGGCGCGACTTTGGAGGGGCGCGGGGCGCGTGGGCGCGGGGCGCGAGGGCGCGGGGCAGGGCGCGATGGGCGCGGGGGGCGCGTATACGACCGGGCGCGCAGGGGGCGCGGGGCGCGTCTTGGGCGCGGGGCGCGAGGGCGCGGGACTATTTGGGGCGCGGGGCGCGGGGCGCGCGGGGCGCGAGGGCGCGGGGGCGCGTCAAGGGCGCGTCGGGCGCGTGGGGCGCGGGGCGCGTTCGAGGTTGGGCGCGACAATTGGGCGCGTCCTAGGGCGCGGGGGCGCGATGGGGGCGCGTGGGCGCGCGTTCGGGCGCGGGGCGCGATGGGGCGCGTACGCGGGCGCGTGGGCGCGGGCGGGCGCGGGGGCGCGGGGCGCGCTTAACGGGCGCGAGGGACGATAACTGGGCGCGTGGGCGCGTGGGCGCGCTTCCAAAAAGGGCGCGGGTTGGGCGCGAGGGCGCGCGGGGCGCGGCGGGCGCGCGGGCGCGAATCGGGCGCGGCGGGCGCGACCGGGCGCGGAACAAGCATGGGCGCGCGAAGGGCGCGGGGCGCGGCGGGCGCGGGGCGCGCACTGGGCGCGCACCGGGCGCGAGGGGGCGCGTCAGGGCGCGATGGGCGCGGGGGCGCGAGGGCGCGTCCGAAGGGCGCGGGGCGCGCGTGGGCGCGGGGCGCGCCACTGGGCGCGGGGGCGCGGGGCGCGAGGGGCGCGTTGGGCGCGCCCGCTATCAGGGCGCGTTGGGCGCGAGGGCGCGAGGGCGCGTCAGACCCAACCGGGCGCGTCGGGCGCGCCAGGGGCGCGGGGCGCGAAACTCGCTGGGCGCGACCATAAGGGCGCGCGAACTGAGGGCGCGCAGGGCGCGAAGGGCGCGGGGCGCGGGGCGCGAGGGGCGCGTGGGGGCGCGAATGGGCGCGAGGGCGCGCCGGGGCGCGGGGCGCGGGGCGCGAGATAGACAAGTCGAATCGGGGCGCGTGGGCGCGACGGGGCGCGGGGGCGCGCGGGCGCGGGCTTGGGCGCGTGGGGCGCGGCGGGCGCGTCGGGCGCGGGGGGCGCGTTCCGGGCGCGCGGGCGCGTGGGCGCGGGGCGCGGGGCGCGGGGCGCGCGGGCGCGCGGGCGCGGAGGGCGCGGAAACCGGGGCGCGCGGGGGCGCGGGGCGCGGGGCGCGAGGGCGCGGGGCGCGGGGGCGCGACGGGCGCGCACGGGCGCGGCGGGCGCGGGGCGCGGAACATGAGTGTGTGTGGGCGCGCTGGGCGCGAGGGCGCGGGGCGCGAAAGGGCGCGGGGCGCGCCTGGCTGGGGCGCGGCAGAGGGCGCGGGGCGCGTGGGCGCGGGGGGGCGCGACTAAACTGGGGCGCGTCGGGGCGCGGCTGCAGGGCGCGGAGAGGGGCGCGGACTCAGGAGGGCGCGCGGGCGCGAAACGTCTTTCGCAGGGCGCGACCCGGGCGCGGGGGCGCGTTGGGGGCGCGGGGCGCGAGGCGGGCGCGCCTGCAAATTGGGGCGCGCCGGGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGTTCGTGGTGGGGCGCGCTGGGCGCGATCGACGGACGGGCGCGAACTCGCGGGCGCGGGGCGCGTGGGGCGCGAGGGCGCGGGGCGCGGGGGCGCGGGGCGCGCTACCGATCGGGGCGCGGGGCGCGAGGGCGCGTTTAAATAGGGGCGCGGCATAGGGCGCGGGGCGCGGCGGGCGCGAGCGGGCGCGTAATGGGCGCGTGGGCGCGTTAAGACCGTTTCCGGGGGCGCGGGGCGCGTGCTGTTGGGCGCGGGCTGGGCGCGGGGCGCGGGGCGCGGGGCGCGGGGCGCGGGCGGGCGCGAGAGGGCGCGTGGGGCGCGGGGCGCGGGGCGCGGCGGGGGGCGCGGGGGGCGCGTCGGGATGGGCGCGTCCTGGGCGCGTGGGCGCGGGGCGCGGGGCGCGCTTCGGGCGCGGCGGGCGCGGGGCGCGATGGGCGCGGGGCGCGCGGGCGCGCGGGCGCGTTCCCTGACTTGAGTCAAAACCGGGTGGGCGCGAGGGCGCGGGGCGCGTAGGGCGCGGGGCGCGTAAAGGGCGCGAGGGCGCGTCTGGGCGCGGGGCGCGCCGGGCGCGTGCTATTGGGCGCGTAGGGCGCGCTGGGCGCGGGGCGCGCAGGGGCGCGTATCTTTGGGCGCGGAGAGGGCGCGGGGCGCGGGGCGCGTGGGCGCGTCAGGGCGCGCGGGCGCGAGCAGGGGCGCGAAAGCCTGGGGCGCGGGCTCGTGGGCGCGGGGCGCGATCAGTGGGCGCGCGCATAGTGCTGAGGGCGCGGGGCGCGTGGGCGCGGGGCGCGACGGGCGCGCTTGGGGCGCGCTGCGGGGCGCGAGGGCGCGGTCAAAGACATGGGCGCG"
#Pattern="GGGCGCGGG"
#data=PatternMatching(Pattern,Genome)
#print(*data, sep=' ')


