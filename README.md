# Basic New Scraper

---
## Simplified Process
```
fetch -> parse -> normalize -> deduplicate -> database
```

## App Options

1. Fetch data from internet
2. Analyze saved data
3. (WIP)

## File Structure
```

├── main.py
├── config.py
├── news_scraper.py
├── analysis
│   ├── text_cleaning.py
│   ├── tfidf.py
│   └── test
│       ├── test_text_sanitize.py
│       └── test_tfidf.py
└── collector
    ├── source.py
    ├── database.py
    ├── parser.py
    └── test
        ├── check_db.py
        ├── test_db_null_read.py
        ├── test_dedup.py
        ├── test_get_articles.py
        └── test_search_articles.py
        
```

## TODO List
- [x] Implement Google RSS fetching 
- [x] Add SQLite
- [x] Write data to SQLite
- [x] Sanitize input data
- [x] Implement text similarity detection
- [ ] Implement embeddings
- [ ] Add basic config file
- [ ] Add Thai language support