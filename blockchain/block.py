import hashlib
class Block:
    def __init__(self, index, timestamp, student_data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.student_data = student_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        block_data = (
            str(self.index)
            + str(self.timestamp)
            + str(self.student_data)
            + str(self.previous_hash)
        )

        return hashlib.sha256(block_data.encode()).hexdigest()