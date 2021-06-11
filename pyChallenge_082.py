poem = ('What is this life if, full of care, We have no time to stand and stare.')
fir_index = int(input('Enter the starting index. (0 ~ %d) : ' %(len(poem) - 1)))
end_index = int(input('Please enter the last index. (%d ~ %d) : ' %(fir_index, len(poem))))
print(poem[fir_index:end_index])
