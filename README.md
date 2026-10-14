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
├── root_dir.py
├── news_scraper.py
├── config.ini
├── analysis
│   ├── text_cleaning.py
│   ├── tfidf.py
│   └── test
│       ├── test_text_sanitize.py
│       └── test_tfidf.py
├── collector
│   ├── source.py
│   ├── database.py
│   ├── parser.py
│   └── test
│       ├── check_db.py
│       ├── test_db_null_read.py
│       ├── test_dedup.py
│       ├── test_get_articles.py
│       └── test_search_articles.py
├── config
│   └── setting.py
└── mode
    ├── analyze.py
    └── collect.py
```

## TODO List
- [x] Implement Google RSS fetching 
- [x] Add SQLite
- [x] Write data to SQLite
- [x] Sanitize input data
- [x] Implement text similarity detection
- [x] Add basic config file
- [x] Add basic landing ui
- [ ] Implement clustering
- [ ] Add Thai language support