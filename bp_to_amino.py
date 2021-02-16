# Amino Acid from bp converter
# Jeff Pearson - Feb 16 2021

bp_to_amino = {
    "UUU": "Phe",
    "UUC": "Phe",
    "UUA": "Leu",
    "UUG": "Leu",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",
    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",
    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",
    "UAU": "Tyr",
    "UAC": "Tyr",
    "UAA": "Stop",
    "UAG": "Stop",
    "CAU": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",
    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "UGU": "Cys",
    "UGC": "Cys",
    "UGA": "Stop",
    "UGG": "Trp",
    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",
    "AGU": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",
    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly"
}

three_to_one = {
    "Ala": "A",
    "Arg": "R",
    "Asn": "N",
    "Asp": "D",
    "Cys": "C",
    "Glu": "E",
    "Gln": "Q",
    "Gly": "G",
    "His": "H",
    "Ile": "I",
    "Lys": "K",
    "Met": "M",
    "Phe": "F",
    "Pro": "P",
    "Ser": "S",
    "Thr": "T",
    "Trp": "W",
    "Tyr": "Y",
    "Val": "V"
}

def find_first_mod_three(rna, pattern):
    end_ind_return = rna.find(pattern)
    while(end_ind_return % 3 != 0 and end_ind_return + 1 <= len(rna) and rna.find(pattern, end_ind_return + 1) > end_ind_return):
        end_ind_return = end_ind_return + 1
        end_ind_return = rna.find(pattern, end_ind_return)
    if(end_ind_return % 3 != 0):
        return -1
    else:
        return end_ind_return


amino_string = input("Enter string of base pairs: ")
amino_string = amino_string.replace("T", "U")
print("Total BP: " + str(len(amino_string)))
start_index = amino_string.find("AUG") # Find start codon
if (start_index == -1):
    print("No start codon detected")
    start_index = 0

amino_string = amino_string[start_index:] # get rid of excess at beginning

end_index_1 = find_first_mod_three(amino_string, "UAA")
end_index_2 = find_first_mod_three(amino_string, "UAG")
end_index_3 = find_first_mod_three(amino_string, "UGA")

if (start_index == -1):
    print("Invalid template strand")
    exit(1)

end_index = -1
if(end_index_1 != -1):
    end_index = end_index_1

if (end_index_2 != -1):
    if(end_index == -1):
        end_index = end_index_2
    elif(end_index_2 < end_index):
        end_index = end_index_2

if (end_index_3 != -1):
    if(end_index == -1):
        end_index = end_index_3
    elif(end_index_3 < end_index):
        end_index = end_index_3

string_of_aminos = ""
one_letter_sequence = ""
try:
    for i in range(0, len(amino_string), 3):
        three_letter_seq = bp_to_amino[amino_string[i:i+3]]
        if(three_letter_seq != "Stop"):
            string_of_aminos = string_of_aminos + three_letter_seq + '-'
            one_letter_sequence += three_to_one[three_letter_seq] 
        else:
            break
except KeyError:
    print("Invalid template strand")
    exit(1)

print("Total Codons: " + str(int(len(amino_string) / 3)))
print("3 Letter Sequence: " + string_of_aminos[:len(string_of_aminos)-1])
print("1 Letter Sequence: " + one_letter_sequence)