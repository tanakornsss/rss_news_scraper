# Basic New Scraper

---
## Simplified Process
```
fetch -> parse -> normalize -> deduplicate -> database
```

## File Structure
```

├── main.py
├── config.py
├── news_scraper.py
├── analysis
│   ├── text_cleaning.py
│   └── test
│       └── test_text_sanitize.py
└── collector
    ├── source.py
    ├── database.py
    ├── parser.py
    └── test
        ├── check_db.py
        ├── test_db_null_read.py
        ├── test_get_articles.py
        └── test_search_articles.py
        
```

## TODO List
- [x] Implement Google RSS fetching 
- [x] Add SQLite
- [x] Write data to SQLite
- [x] Sanitize input data
- [ ] Implement TF-IDF
- [ ] Implement cosine similarity