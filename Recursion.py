
class PermutationChecker: #does it need to be a class here?
    """
    referenced MY OWN leetcode solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, match = Counter(s1), len(s1), 0     

        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]: match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]]: match += 1

            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]: match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]]: match += 1

            if match == len(cntr):
                return True

        return False
    """
    def checkPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        w = len(s1)
        s1_count = [0] * 26
        window_count = [0] * 26
        
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
            
        for i in range(len(s2)):
            r_idx = ord(s2[i]) - ord('a')
            window_count[r_idx] += 1
            
            if i >= w:
                l_idx = ord(s2[i - w]) - ord('a')
                window_count[l_idx] -= 1
                
            if s1_count == window_count:
                return True
                
        return False

class EightQueensSolver:
    def __init__(self):
        self.solutions = []
        self._find_solutions(0, [])

    def _find_solutions(self, col, board):
        if col == 8:
            self.solutions.append(list(board))
            return
        
        for r in range(1, 9):
            safe = True
            for i, b in enumerate(board):
                if b == r or abs(b - r) == col - i:
                    safe = False
                    break
            if safe:
                board.append(r)
                self._find_solutions(col + 1, board)
                board.pop()

    def minMovesToValidQueens(self, input_data) -> int:
        # convert input to a list of ints
        queens = [int(x) for x in input_data.split()]
            
        min_moves = 8
        
        # Compare against every valid 8-queens board layout
        for sol in self.solutions:
            moves = 0
            for i in range(8):
                if queens[i] != sol[i]:
                    moves += 1
            if moves < min_moves:
                min_moves = moves
                
        return min_moves