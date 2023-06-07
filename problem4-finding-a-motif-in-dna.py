# https://rosalind.info/problems/subs/

seq = input()
sub_seq = 'GTAGTGTGT'
index = 0
found_indices = []
while index < len(seq):
    index = seq.find(sub_seq, index)
    if index == -1:
        break
    found_indices.append(index+1)
    index += 1

print(*found_indices)

