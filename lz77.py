"""
Lz77 coding alghorithm
"""
class Lz77:
    """
    Lz77 coding alghorithm
    """
    def __init__(self, buffer):
        self.buffer_size=buffer
    def encode(self, data):
        """
        Encode a string using lz77
        """
        codings=[]
        buffer=""
        while len(data)!=0:
            match,ind=self.find_best_match(data,buffer)
            if match:
                data=data[len(match):]
                codings.append((ind,len(match),data[0] if data else ""))
                buffer+=match+data[0] if data else match
                buffer=buffer[-self.buffer_size:]
                data=data[1:]
            else:
                codings.append((0,0,data[0]))
                buffer+=data[0]
                buffer=buffer[-self.buffer_size:]
                data=data[1:]
        return codings
    def find_best_match(self, data, buffer):
        """
        Finds longest match between data and buffer
        """
        if not data or not buffer:
            return "",None
        _match=""
        max_ind=0
        if buffer==data[:len(buffer)]:
            for i,el in enumerate(data):
                if el==buffer[i%len(buffer)]:
                    _match+=el
                else:
                    break
            return _match, len(buffer)
        for i,el in enumerate(buffer):
            curr_match=""
            if el==data[0]:
                curr_match=el
                ind=0
                for j in range(i+1,len(buffer)):
                    ind+=1
                    if ind+1<=len(data) and data[ind]==buffer[j]:
                        curr_match+=data[ind]
                    else:
                        break
                if len(curr_match)>len(_match):
                    _match=curr_match
                    max_ind=i
        return _match, len(buffer)-max_ind

    def decode(self, data):
        """
        Decode a string using lz77
        """
        msg=""
        for el in data:
            if el[0]==0:
                msg+=el[2]
            else:
                if el[1]>el[0]:
                    div=el[1]//el[0]
                    mod=el[1]%el[0]
                    msg+=msg[-el[0]:]*div+msg[-el[0]:-el[0]+mod]
                    el=el[0],el[1]%el[0],el[2]
                msg+=msg[-el[0]:len(msg)-el[0]+el[1]]+el[2]
        return msg
if __name__=='__main__':
    lz=Lz77(10000)
    msh=lz.encode("aababcabcabcabcabcabc")
    print(lz.decode(msh)=="aababcabcabcabcabcabc")
    print(lz.decode(msh))
    print("aababcabcabcabcabcabc")
    print(lz.decode(lz.encode("icanttakeitanymoreee")))
    lorem_ipsum="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
 ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
 ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
 velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
 cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
    print(lz.decode(lz.encode(lorem_ipsum))==lorem_ipsum)
    eneida=""""""
    with open("Coding-Algorithms/eneida.txt",'r',encoding='utf-8') as f:
        eneida=f.read()
    encoded=lz.encode(eneida)
    print(lz.decode(encoded)==eneida)
