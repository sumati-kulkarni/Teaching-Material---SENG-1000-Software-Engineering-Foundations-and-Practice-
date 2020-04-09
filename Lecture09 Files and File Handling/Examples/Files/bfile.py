f = open('bfile.txt', 'rb+')
f.write(b'0123456789abcdef')
f.close()

with open('bfile.txt', 'rb+') as f:
    print("6th byte --> ", f.seek(5))      # Go to the 6th byte in the file
    print("read first byte from seeked position --> ", f.read(1))
    print("Go to the 3rd byte in reverse direction --> ", f.seek(-8, 2))  # Go to the 3rd byte before the end
    print("read first byte from seeked position --> ", f.read(1))

