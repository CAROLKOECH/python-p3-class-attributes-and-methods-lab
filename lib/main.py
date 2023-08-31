from song import Song

# Creating song instances
song1 = Song("Song 1", "Artist 1", "Genre 1")
song2 = Song("Song 2", "Artist 2", "Genre 2")
song3 = Song("Song 3", "Artist 1", "Genre 1")

# Displaying class attributes and counts
print("Total Songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre Count:", Song.genre_count)
print("Artist Count:", Song.artist_count)
