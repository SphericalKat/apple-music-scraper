# Apple music scraper
To get started, follow the steps below

1. Create a virtual environment
```bash
python3 -m venv venv
source ./venv/bin/activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the scraper
```bash
scrapy crawl album -a album=<albumid>
```

eg: `scrapy crawl album -a album=1702773361`