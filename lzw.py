"""
LZW encoding algorithm
"""
class LZW:
    """
    LZW
    """
    @staticmethod
    def encode(data):
        """
        LZW encoding
        """
        if not data:
            return []
        decode_dict={sym: i for i,sym in enumerate(sorted(list(set(data))))}
        curr_char=data[0]
        encoded_text=[]
        for i,_ in enumerate(data):
            next_char=data[i+1] if i!=len(data)-1 else ""
            if curr_char+next_char in decode_dict:
                curr_char+=next_char
            else:
                encoded_text.append(decode_dict[curr_char])
                decode_dict[curr_char+next_char]=max(decode_dict.values())+1
                curr_char=next_char
        encoded_text.append(decode_dict[curr_char])
        return encoded_text, {v:k for k,v in decode_dict.items()}
    @staticmethod
    def decode(data,decode_dict):
        """
        LZW decoding
        """
        curr_code=data[0]
        curr_char=decode_dict[curr_code]
        tmp=curr_char[0]
        decoded=curr_char
        for i in range(len(data)-1):
            next_char=data[i+1]
            if next_char not in decode_dict:
                curr_char=decode_dict[curr_code]+tmp
            else:
                curr_char=decode_dict[next_char]
            decoded+=curr_char
            tmp=curr_char[0]
            decode_dict[max(decode_dict)+1]=decode_dict[curr_code]+tmp
            curr_code=next_char
        return decoded
if __name__=='__main__':
    print(LZW.decode(*LZW.encode('aaaaa')))
