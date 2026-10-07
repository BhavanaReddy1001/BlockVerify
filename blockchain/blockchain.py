from blockchain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            0,
            "2026-10-07 10:00:00",
            {
                "student_id": "GENESIS",
                "name": "Genesis Block",
                "course": "Blockchain System",
                "semester": 0,
                "cgpa": 0.0
            },
            "0"
        )

        self.chain.append(genesis_block)

    def add_block(self, student_data, timestamp):
        previous_block = self.chain[-1]

        new_block = Block(
            len(self.chain),
            timestamp,
            student_data,
            previous_block.hash
        )

        self.chain.append(new_block)

    def get_latest_block(self):
        return self.chain[-1]
    def get_chain(self):
        return self.chain

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
               return False

            if current_block.previous_hash != previous_block.hash:
               return False

        return True