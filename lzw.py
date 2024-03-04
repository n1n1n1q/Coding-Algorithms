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
        decode_dict={i:chr(char_ord) for i, char_ord in enumerate(range(ord('a'),ord('z')+1))}
        return decode_dict
    @staticmethod
    def decode(data):
        """
        LZW decoding
        """
        decode_dict={i:chr(char_ord) for i, char_ord in enumerate(range(ord('a'),ord('z')+1))}
        return decode_dict

if __name__=='__main__':
    print(LZW.decode('a'))
