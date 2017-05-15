winstreak = 0
losingstreak = 0


print("Welcome back. You've won",winstreak,"in a row.")


def main():
        winloss = input("Did you win? 1 yes 2 if no: ")
        if winloss == 1:
                win = win + 1
                winstreak = winstreak + 1
		print("Your losing streak of",losingstreak,"has been reset")
		losingstreak = 0
	elif winloss == 2:
		loss = loss + 1
		losingstreak = losingstreak + 1
	return

main()
			
