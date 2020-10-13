import collections
def solver(array, threshold):
	user_count = collections.defauldict()
	for log in array:
		for user in set(log.split(" ")[:2]):
			user_count[user] += 1
	return sorted([user for user, count in user_count.items() if count > threshold])