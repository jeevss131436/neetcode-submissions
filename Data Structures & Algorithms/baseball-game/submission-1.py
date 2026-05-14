class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for index in range(len(operations)):
            if (operations[index] == "+"):
                record.append(int(record[len(record) - 1]) + int(record[len(record) - 2]))
            elif (operations[index] == "C"):
                record.pop()
            elif (operations[index] == "D"):
                record.append(int(record[len(record) - 1]) * 2)
            else:
                record.append(int(operations[index]))
        return sum(record)