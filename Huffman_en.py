#Huffman Encoding
from Huffman_Node import Node

class Huffman_encoding:

    #create nodes创建叶子节点
    def createNodes(freqs):
        return [Node(freq) for freq in freqs]

    #create Huffman-Tree创建Huffman树
    def createHuffmanTree(nodes):
        queue = nodes[:]
        while len(queue) > 1:
            queue.sort(key=lambda item:item.freq)
            node_left = queue.pop(0)
            node_right = queue.pop(0)
            node_father = Node(node_left.freq + node_right.freq)
            node_father.left = node_left
            node_father.right = node_right
            node_left.father = node_father
            node_right.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]
#Huffman编码
    def huffmanEncoding(nodes,root):
        codes = [''] * len(nodes)
        for i in range(len(nodes)):
            node_tmp = nodes[i]
            while node_tmp != root:
                if node_tmp.isLeft():
                    codes[i] = '0' + codes[i]
                else:
                    codes[i] = '1' + codes[i]
                node_tmp = node_tmp.father
        return codes

    def start_encoding(self,address_in,address_out):
        #读取存放的文件
        S_in = open(address_in)  # 打开存放数组的文件
        str_= S_in.readlines()  # 这是一个字符串数组
        # print(str)
        length = len(str_)  # 字符串数组的长度
        p = [[0 for m in range(2)] for n in range(length)]
        for i in range(length):
            lis1 = str_[i][:]  # 定义变量保存数组中每一行的值
            lis2 = lis1.split(" ")  # 将每一行的值按空格进行分割
            lis2[1] = int(lis2[1])
            print(lis2)
            p[i] = lis2
            # lis3= list(map(float,lis2))
            # p[i] = list(lis3)
        S_out=open(address_out,"a")
        #开始加密
        chars_freqs = p
        nodes = self.createNodes([item[1] for item in chars_freqs])
        root = self.createHuffmanTree(nodes)
        codes = self.huffmanEncoding(nodes,root)
        for item in zip(chars_freqs,codes):
            S_out.writelines("字符:"+item[0][0]+" 编码结果:"+str(item[1])+"\n")
#           print('Character:%s freq:%-2d   encoding: %s' % (item[0][0],item[0][1],item[1]))
#        S_out.writelines("最终结果是：")
        for item in zip(chars_freqs,codes):
            S_out.writelines(str(item[1]))

