def isAnagram(s, t):
	return collections.Counter(s) == collections.Counter(t)
	