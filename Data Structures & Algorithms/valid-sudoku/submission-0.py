class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = defaultdict(set) # making a hashset for columns
        rows = defaultdict(set) # making a hashset for rows
        squares = defaultdict(set) # # making a hashset for particular block or square

        for r in range(9):  # iterating over rows
            for c in range(9): # iterating over cols
                if board[r][c] == '.':  # checking if the cell is empty
                    continue    # if yes then simply move to next cell
                if (board[r][c] in rows[r] or   # check in all the 3 hash sets as per sudoku rule, first is rows
                    board[r][c] in cols[c] or   # then we check in cols too
                    board[r][c] in squares[(r//3,c//3)]):   # finally for the whole block, 
                    # why //3 to as we know each block is 3x3 grid so find out the particular cell of particular block makes it easier with //3
                    return False    # if yes, return False
                else:   # or else
                    rows[r].add(board[r][c])    # add it in the all the hash sets
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        return True     # after successful iterating if no False return found, simply return True