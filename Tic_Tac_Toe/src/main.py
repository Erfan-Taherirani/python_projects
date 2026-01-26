import random


class TicTacToe:
	def __init__(self):
		self.board = [" "] * 10 # 0th element ignored
		self.player_turn = self.get_random_player_turn()

	def __str__(self) -> str:
		txt1 = f"\n{self.board[1]} | {self.board[2]} | {self.board[3]}\n----------"
		txt2 = f"\n{self.board[4]} | {self.board[5]} | {self.board[6]}\n----------"
		txt3 = f"\n{self.board[7]} | {self.board[8]} | {self.board[9]}\n"
		return txt1 + txt2 + txt3

	def show_board(self):
		print("\n")
		print(f"{self.board[1]} | {self.board[2]} | {self.board[3]}")
		print("-" * 10)
		print(f"{self.board[4]} | {self.board[5]} | {self.board[6]}")
		print("-" * 10)
		print(f"{self.board[7]} | {self.board[8]} | {self.board[9]}")
		print("\n")

	def swap_player_turn(self):
		self.player_turn = "O" if self.player_turn == "X" else "X"

	def get_random_player_turn(self):
		self.player_turn = random.choice(["X", "O"])
		return self.player_turn
	
	def fix_spot(self, player, cell):
		self.board[cell] = player

	def has_player_won(self, player):
		win_combinations = [
			[1, 2, 3], [4, 5, 6], [7, 8, 9], # row combinations
			[1, 4, 7], [2, 5, 8], [3, 6, 9], # column combinations
			[1, 5, 9], [3, 5, 7] # diagonal combinations
		]

		for combination in win_combinations:
			if all(self.board[i] == player for i in combination):
				return True
			
		return False

	def is_board_filled(self):
		return ' ' not in [self.board[i] for i in range(1, 10)]
	
	def play(self):
		while True:
			print(self)
			print(f"This is player {self.player_turn}'s turn.")
			cell = input("Please enter a cell from 1 to 9: ")

			if (int(cell) in range(1, 10)) and (self.board[int(cell)] == " "):
				self.fix_spot(self.player_turn, int(cell))
			else:
				print("Enter a valid cell!")

			if self.has_player_won(self.player_turn):
				print(f"player {self.player_turn} won!")
				break

			if self.is_board_filled():
				print("Tie")
				break
			
			self.swap_player_turn()
if __name__ == "__main__":
	game = TicTacToe()
	game.play()
