e2cDict = {}
c2eDict = {}

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tmp   = alpha
chains = []

# Iterate through the alphabet until no characters remain
while len(tmp) != 0:
	# Current char is whatever is first in tmp
	curr = tmp[0]
	# Immediately remove curr from tmp so we don't repeat chars
	tmp = tmp.replace(curr, "")
	# Set chain to starting character
	chain = curr

	while True:
		# Check if current character has a corresponding encoded character
		# And check if that character has already been used.
		# Break on fail- either we've hit the end of the chain or we're in an infinite loop
		if curr in c2eDict and c2eDict[curr] in tmp:
			chain += c2eDict[curr]
			curr = c2eDict[curr]
			tmp = tmp.replace(curr,"")
		else:
			break

	while True:
		# Repeat same process as above, but in the opposite direction
		if curr in e2cDict and e2cDict[curr] in tmp:
			chain = e2cDict[curr] + chain
			curr = e2cDict[curr]
			tmp = tmp.replace(curr,"")
		else:
			break

	# If the chain is greater than one character, append it to the list of chains
	if len(chain) > 1:
		chains.append(chain)

return chains
