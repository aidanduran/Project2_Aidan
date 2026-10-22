levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

for info in range(len(levels)):
    print(f"Level {levels[info]}\nCoins: {coins[info]}\nEnemies: {enemies[info]}\nPower-Up: {power_ups[info]}\n")

player_Name = "Hero"
lives = 3
score = 0
total_coins = 0

print(f"Player: {player_Name}\nLives: {lives}\nScore: {score}\nTotal Coins: {total_coins}\n")

level_scores = []

for info in range(len(levels)):
    if power_ups[info] == "Star":
        level_scores.append((coins[info] * 10) + (enemies[info] * -5) + 25)
    else:
        level_scores.append((coins[info] * 10) + (enemies[info] * -5))

for level in range(len(level_scores)):
    print(f"Level {level} score: {level_scores[level]}")