from block import Block


class Blockchain:
    """
    blockchain: a public ledger of transactions.
    implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self):
        return f"Blockchain: {self.chain}"

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))


def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)
    print(f"blockchain.py __name__ is set to: {__name__}")


if __name__ == "__main__":
    main()