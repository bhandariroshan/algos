import hashlib


def calc_hash(string):
    sha = hashlib.sha256()
    hash_str = string.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(data)
        self.next = None


class BlockChain:
    def __init__(self, block):
        self.block = block

    def add_block(self, new_block):
        block = self.block

        while block.next != None:
            block = block.next

        new_block.previous_hash = block.hash
        block.next = new_block

    def get_block(self, position):
        count = 1
        block = self.block
        while count < position:
            count += 1
            block = block.next

        if block:
            return block.data, block.previous_hash, block.hash
        else:
            return None, None, None



def test():
    # Test Cases
    block_chain = BlockChain(Block('1-30-2021', 'My name is Roshan. '))
    block_chain.add_block(Block('1-30-2021', 'My last name is Bhandari.'))
    block_chain.add_block(Block('1-30-2021', 'I am a computer science major. '))
    block_chain.add_block(Block('1-30-2021', 'I live in South Carolina. '))

    # check block 1
    print ("Pass" if ('My name is Roshan. ' == block_chain.get_block(1)[0]) else "Fail")
    
    # check block 2
    print ("Pass" if ('My last name is Bhandari.' == block_chain.get_block(2)[0]) else "Fail")
    
    # get block 3
    print ("Pass" if ('I am a computer science major. ' == block_chain.get_block(3)[0]) else "Fail")
    
    # get block 4
    print ("Pass" if ('I live in South Carolina. ' == block_chain.get_block(4)[0]) else "Fail")
    
    # check edge case
    print ("Pass" if (None == block_chain.get_block(5)[0]) else "Fail")

    # check hash of 3 == previous hash of 4
    print ("Pass" if (block_chain.get_block(3)[2] == block_chain.get_block(4)[1]) else "Fail")


if __name__ == "__main__":
    test()