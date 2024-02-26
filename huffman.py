"""
Huffman coding algorithm
"""
from heapq import heappush, heappop
class Node:
    """
    Node class
    """
    def __init__(self, freq, char, left=None, right=None):
        self.char=char
        self.freq=freq
        self.left=left
        self.right=right
        self.direction=""
    def __lt__(self, other):
        return self.freq<other.freq
class Huffman:
    """
    Huffman coding algorithm
    """
    def __init__(self):
        pass
    def encode(self, data):
        """
        Huffman encode
        """
        frequencies=self.frequency(data)
        nodes=[]
        for k,v in frequencies.items():
            heappush(nodes,Node(v,k))
        while len(nodes)!=1:
            nodes.sort(key=lambda x:x.freq)
            left=heappop(nodes)
            right=heappop(nodes)
            left.direction="0"
            right.direction="1"
            heappush(nodes,Node(left.freq+right.freq, left.char+right.char, left, right))
        codes=dict(sorted(self.build_tree(nodes[0]).items(), key=lambda x:x[1],reverse=True))
        encoded_data=''.join(list(map(lambda x:codes[x], data)))
        return encoded_data,codes
    def build_tree(self, node, code=""):
        """
        Build huffman tree
        """
        codes={}
        code+=node.direction
        if node.left:
            left=self.build_tree(node.left, code)
            codes.update(left)
        if node.right:
            right=self.build_tree(node.right, code)
            codes.update(right)
        if not node.left and not node.right:
            codes[node.char]=code
        return codes

    def frequency(self, data):
        """
        Find each char's frequency
        """
        freq={}
        for i in set(data):
            freq[i]=data.count(i)
        return freq
    def decode(self, data, dictionary):
        """
        Huffman decode
        """
        decoded_data=""
        tmp=""
        for char in data:
            tmp+=char
            if tmp in dictionary.values():
                decoded_data+=list(dictionary.keys())[list(dictionary.values()).index(tmp)]
                tmp=""
        return decoded_data
    @staticmethod
    def calculate_compression(compressed_data, original_data):
        """
        Calculate compression ratio
        """
        return (8*len(original_data))/len(compressed_data)*100

if __name__=='__main__':
    g=Huffman()
    data="daaaab"
    print(g.encode(data))
    print(g.decode(*g.encode(data)))
    print(Huffman.calculate_compression(g.encode(data)[0], data))
    print(g.encode(data)[0],data)
    eneida=""
    with open("eneida.txt",'r',encoding='utf-8') as file:
        eneida=file.read()
    encoded=g.encode(eneida)
    print(Huffman.calculate_compression(encoded[0], eneida))
    print(g.decode(*encoded)==eneida)
