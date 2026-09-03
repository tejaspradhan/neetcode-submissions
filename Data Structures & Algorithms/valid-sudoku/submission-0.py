class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check for duplicates in rows
        for row in board:
            if self.containsDuplicates(row):
                return False
        
        # Check for duplicates in columns
        for i in range(9):
            col = [row[i] for row in board]
            if self.containsDuplicates(col):
                return False
        
        # Check for duplicates in grids
        
        grids = {}
        for i in range(9):
            grids[i] = []

        for i in range(len(board)):
            print(grids)
            for j in range(len(board[i])):
                if not board[i][j].isalnum():
                    continue
                index = ((i)//3)*3 + (j)//3
                if board[i][j] in grids[index]:
                    return False
                grids[index].append(board[i][j])
        
        return True
    
    def containsDuplicates(self,nums: List):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            elif n.isalnum():
                seen.add(n)
        return False

        
        

        