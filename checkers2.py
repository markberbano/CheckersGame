class Board(object):
	
	board= [[' ' for row in range(1,9)] for col in range(1,9)]
	
	def __init__(self):
		#Initializes the start of the game with 12 checkers on each side
		for row_index, row in enumerate(self.board, start=1):
			for col_index, col in enumerate(row, start=1):
				if row_index<4:
					if row_index%2 == 0 and col_index%2 == 0:
							row[col_index-1]='X'

					if row_index%2 == 1 and col_index%2 == 1:						
							row[col_index-1]='X'
							
				elif 3<row_index<6:
					if row_index == 4 and col_index%2 == 0:
							row[col_index-1]='.'
				
					if row_index == 5 and col_index%2 == 1:						
							row[col_index-1]='.'
							
				elif row_index>5:
					if row_index%2 == 0 and col_index%2 == 0:						
							row[col_index-1]='O'
						
					if row_index%2 == 1 and col_index%2 ==1:				
							row[col_index-1]='O'
	
	
	def printboard(self):
		print('  0  1  2  3  4  5  6  7')
		for row_index,rows in enumerate(self.board):	
			print(row_index,'  '.join(rows))
			
			
	def valid_move(self, start, end):
		#Checks to see whether a move is valid, can only move to '.' diagonal spots one space ahead
		if self.board[end[0]][end[1]] == '.' and self.board[start[0]][start[1]] == 'X' and end[0] == start[0]+1:
			return(True)
		
		if self.board[end[0]][end[1]] == '.' and self.board[start[0]][start[1]] == 'O' and end[0] == start[0]-1:
			return(True)
			
		else:
			return(False)
			
			
	def valid_jump(self, start, jumpover, end):
		#Checks if checkers to jump and capture other checkers, can only jump over diagonal opposing checkers to a '.' diagonal spot
		if self.board[start[0]][start[1]] == 'X' and self.board[jumpover[0]][jumpover[1]] == 'O' and jumpover[0] == start[0]+1 and end[0] == start[0]+2:
			return(True)
			
		if self.board[start[0]][start[1]] == 'O' and self.board[jumpover[0]][jumpover[1]] == 'X' and jumpover[0] == start[0]-1 and end[0] == start[0]-2:
			return(True)
			
		else: return(False)
			
			
	def king(self, start, endrow):
		#Converts a checker into a king once it reaches the opposite end of the board 
		if self.board[start[0]][start[1]] == 'X' and self.board[endrow[0]] == 7:
			return(True)
			
		if self.board[start[0]][start[1]] == 'O' and self.board[endrow[0]] == 0:	
			return(True)
		
		else: return(False)
					
	
	def move(self, start, end):
		if self.valid_move(start, end) == True:
			self.board[end[0]][end[1]]=self.board[start[0]][start[1]]
			self.board[start[0]][start[1]]='.'	
		
		else: print('Not a valid move')
		
		#self.king(start, end)
			
		self.printboard()
			
			
	def jump(self, start, jumpover, end):
		#It is up to the player to continuously jump if possible and to decide between multiple jumps, this is not built into the code
		if self.valid_jump(start, jumpover, end) == True:
			self.board[end[0]][end[1]]=self.board[start[0]][start[1]]
			self.board[jumpover[0]][jumpover[1]]='.'
			self.board[start[0]][start[1]]='.'
		
		else: print('Not a valid jump')
		
		self.king(start, end)
		
		self.printboard()
	
	def test(self):
		self.board[0][0]='.'
		self.board[2][2]='O'
		self.board[7][7]='.'
		self.board[5][5]='X'
		
		self.move()
		
		self.printboard()
	
		
board=Board()


		