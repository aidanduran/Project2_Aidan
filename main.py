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

for level in range(len(levels)):
    print(f"Level {levels[level]} score: {level_scores[level]}")
print()

actions = [0, 1, 0, 2, 1]
action_results = []

for action in range(len(actions)):
    if actions[action] == 0:
        action_results.append("Collect Coins")
    elif actions[action] == 1:
        action_results.append("Fight Enemies")
    elif actions[action] == 2:
        action_results.append("Use Power-Up")

for level in range(len(levels)):
    print(f"Level {levels[level]}: {action_results[level]}")
print("")

life_history = []

for level in range(len(levels)):
    if enemies[level] >= 4:
        if power_ups[level] != "Star":
            lives -= 1

    life_history.append(lives)

for level in range(len(levels)):
    print(f"After Level {levels[level]}: {life_history[level]} lives")
print("")

total_coins = sum(coins)

bonus_coin_levels = [coin for coin in coins if coin >= 7]

print(f"Coins collected: {total_coins}")
print(f"Levels with 7 or more coins: {bonus_coin_levels}\n")

inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]

print(f"Starting Inventory: {inventory}")
print(f"Used Power-Ups: {used_powerups}")

inventory.pop(0)
inventory.pop(0)

print(f"Remaining Inventory: {inventory}\n")

print(f"Total Coins: {sum(coins)}")
print(f"Most Coins in One Level: {max(coins)}")
print(f"Fewest Coins in One Level: {min(coins)}")
print(f"Average Coins per Level: {sum(coins) / len(coins)}")
print(f"Total Enemies: {sum(enemies)}")
print(f"Most Enemies in One Level: {max(enemies)}\n")

high_scores = [score for score in level_scores if score >= 50]
print(f"Scores of 50 or Higher: {high_scores}")