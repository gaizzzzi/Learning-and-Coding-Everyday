import collections
def solver(songs):
	song_count = collections.defaultdict(int)
	ans = 0
	for song in songs:
		if (60 - song) % 60 in song_count:
			ans += song_count[(60 - song) % 60]
		song_count[song % 60] += 1
	print(ans)
	return ans
#songs, ans = [37, 23, 60], 1
#songs, ans = [10, 50, 90, 30], 2
#songs, ans = [30, 20, 150, 100, 40], 3
songs, ans = [60, 60, 60], 3
print(solver(songs) == ans)