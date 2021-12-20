import art
from os import system
from random import randint
from game_data import data

def clear_screen():
	system('clear')

def random_profile():
	rand_num = randint(0, len(data) - 1)
	return data[rand_num]

def has_higher_followers(A, B):
	if A['follower_count'] > B['follower_count']:
		return 'A'
	else:
		return 'B'

is_game_over = False
score = 0
profile_A = random_profile()
profile_B = random_profile()
print(art.logo)
while not is_game_over:
	while profile_A == profile_B:
		profile_B = random_profile()
	print(f"Compare A: {profile_A['name']}, {profile_A['description']}, from {profile_A['country']}")
	print(art.vs)
	print(f"Against B: {profile_B['name']}, {profile_B['description']}, from {profile_B['country']}")
	highest_followers = has_higher_followers(profile_A, profile_B)
	choice = input("Who has more followers? 'A' or 'B':")
	if choice == highest_followers:
		clear_screen()
		score += 1
		print(art.logo)
		print(f"You're right! Current Score: {score}")
		profile_A = profile_B
		profile_B = random_profile()
	else:
		is_game_over = True
		clear_screen()
		print(art.logo)
		print(f"Sorry, that’s wrong. Final Score: {score}")