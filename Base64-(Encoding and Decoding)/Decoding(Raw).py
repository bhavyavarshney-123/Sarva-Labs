input=input("Enter a Valid base64 to convert into string:")

def decode_base64(input):
#removing '=' from the given base64 string 
  input = input.replace('=', '')
#conversion to binary string from the base64 Table
  base64_dict = {"110000": "w", "110001": "x", "110101": "1", "110100": "0", "010100": "U", "010101": "V", "001100": "M", "001101": "N", "011110": "e", "011111": "f", "001001": "J", "001000": "I", "011011": "b", "011010": "a", "000110": "G", "000111": "H", "000011": "D", "000010": "C", "100100": "k", "100101": "l", "111100": "8", "111101": "9", "100010": "i", "100011": "j", "101110": "u", "101111": "v", "111001": "5", "111000": "4", "101011": "r", "101010": "q", "110011": "z", "110010": "y", "010010": "S", "010011": "T", "010111": "X", "010110": "W", "110110": "2", "110111": "3", "011000": "Y", "011001": "Z", "001111": "P", "001110": "O", "011101": "d", "011100": "c", "001010": "K", "001011": "L", "101101": "t", "000000": "A", "000001": "B", "100111": "n", "100110": "m", "000101": "F", "000100": "E", "111111": "/", "111110": "+", "100001": "h", "100000": "g", "010001": "R", "010000": "Q", "101100": "s", "111010": "6", "111011": "7", "101000": "o", "101001": "p"}
  binary = ""
  for i in input:
    for k, v in base64_dict.items():
        if v == i:
         z = "".join(k)
         binary += z
  #breaking it into 8 bits(as per convention) and removing extra 0
  binary = [binary[i:i+8] for i in range(0, len(binary), 8)]
  if len(binary[-1]) != 8:
    binary.pop()
  #convert binary to decimal
  ct_decode=[]
  for x in binary:
   ct_decode.append(int(x, 2))
 #convert decimal to String
  output=" "
  for i in ct_decode:
    output+=chr(i)
  return output

#Printing the output
print(decode_base64(input))
