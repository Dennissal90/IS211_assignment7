import random
import sys

random.seed(0)

class Die:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
    
    def reset(self):
        self.total_score = 0

class Game:
    def __init__(self, num_players=2):
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.die = Die()
        self.current_player_index = 0
    
    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def play_turn(self, player):
        turn_score = 0
        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}.")
            if roll == 1:
                print(f"Sorry, {player.name}, you scored nothing this turn.")
                break
            else:
                turn_score += roll
                print(f"Current turn score: {turn_score}, Total score: {player.total_score}")
                decision = input("Roll again or hold? (r/h): ").strip().lower()
                if decision == 'h':
                    player.total_score += turn_score
                    print(f"{player.name} holds with a turn score of {turn_score}, total score: {player.total_score}.")
                    break
    
    def reset_game(self):
        for player in self.players:
            player.reset()
        self.current_player_index = 0
    
    def play_game(self):
        while True:
            self.reset_game()
            while all(player.total_score < 100 for player in self.players):
                current_player = self.players[self.current_player_index]
                print(f"\n{current_player.name}'s turn:")
                self.play_turn(current_player)
                if current_player.total_score >= 100:
                    print(f"{current_player.name} wins with a score of {current_player.total_score}!")
                    break
                self.switch_player()
            play_again = input("\nPlay another game? (yes/no): ").strip().lower()
            if play_again != 'yes':
                break

if __name__ == "__main__":
    num_players = 2
    if "--numPlayers" in sys.argv:
        try:
            num_players_index = sys.argv.index("--numPlayers") + 1
            num_players = int(sys.argv[num_players_index])
        except (ValueError, IndexError):
            print("Invalid number of players provided. Using 2 players by default.")
    
    game = Game(num_players=num_players)
    game.play_game()
