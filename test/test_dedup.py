from collector.database import Database

db = Database()

# This test only works when the database IS EMPTY

article = {
    "title": "Test article",
    "url": "https://example.com/",
    "pub_date": None,
    "scraped_date": "2026-10-11T10:00:00+00:00",
    "source": "Test Source",
}

# First save
first = db.write_to_db([article])

# Second save
second = db.write_to_db([article])

print("First insert:", first)
print("Second insert:", second)

assert first == 1, "First insert should add one row"
assert second == 0, "Duplicate URL should not add another row"

results = db.search_articles("Test article")
print("Search results:", len(results))

assert len(results) >= 1, "Article should be searchable"

print("All tests passed!")
