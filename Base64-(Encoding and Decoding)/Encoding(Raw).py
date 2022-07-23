#base64 table(binary-base64)
base64_dict = {"110000": "w", "110001": "x", "110101": "1", "110100": "0", "010100": "U", "010101": "V", "001100": "M", "001101": "N", "011110": "e", "011111": "f", "001001": "J", "001000": "I", "011011": "b", "011010": "a", "000110": "G", "000111": "H", "000011": "D", "000010": "C", "100100": "k", "100101": "l", "111100": "8", "111101": "9", "100010": "i", "100011": "j", "101110": "u", "101111": "v", "111001": "5", "111000": "4", "101011": "r", "101010": "q", "110011": "z", "110010": "y", "010010": "S", "010011": "T", "010111": "X", "010110": "W", "110110": "2", "110111": "3", "011000": "Y", "011001": "Z", "001111": "P", "001110": "O", "011101": "d", "011100": "c", "001010": "K", "001011": "L", "101101": "t", "000000": "A", "000001": "B", "100111": "n", "100110": "m", "000101": "F", "000100": "E", "111111": "/", "111110": "+", "100001": "h","100000": "g", "010001": "R", "010000": "Q", "101100": "s", "111010": "6", "111011": "7", "101000": "o", "101001": "p"}
#input string
message =input("Enter a string to convert into base64:")
#converting string to ascii value
ascii_values = []
for char in message:
    ascii_values.append(ord(char))
#conversion to binary string from Ascii Values
binary=""
for i in ascii_values:
        z= f'{i:08b}'
        binary+=z
#binary string to serialized string
def biniaryserealization(binary):
    split= [binary[i:i + 6] for i in range(0, len(binary), 6)]
    output = " "
    arr = list()
#spliting the binary string in a pack of 6 and appending in a list    
    for ch in split:
        if(len(ch)!=6):
            while(len(ch)!=6):
                ch = ch+'0'
        arr.append(ch)
#changing the key:"binary string" to value:"base64"       
    for val in arr:
      for k, v in base64_dict.items(): 
        if k == val:
          output+=base64_dict[k]
    if len(binary)%3!=0:
        output+='='
    return output
#Printing the base64 encoded     
print(biniaryserealization(binary))
