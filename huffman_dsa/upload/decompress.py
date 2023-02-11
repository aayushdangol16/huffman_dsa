import ast

def hdecompress(fname):
    path="media/"+fname
    file=open(path,"rb")
    bit_string = ""
    reverse_mapping={}
    byte = file.read(1)
    while(len(byte) > 0):
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0')
        bit_string += bits
        byte = file.read(1)
    padded_encoded_text=bit_string
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)
    padded_encoded_text = padded_encoded_text[8:] 
    encoded_text = padded_encoded_text[:-1*extra_padding]
    file=open("media/reverse_mapping.txt","r")
    f=file.read()
    reverse_mapping=ast.literal_eval(f)
    file.close()
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if(current_code in reverse_mapping):
            character = reverse_mapping[current_code]
            decoded_text += character
            current_code = ""

    dpath="media/decompress.txt"
    file=open(dpath,"w")
    file.write(decoded_text)
    file.close()
    return(dpath)
