# Test Task for Senior Scraping Developer

The purpose of this task is to demonstrate developer's skills in the scraping and building API for operating scraped data.

Developer should demonstrate his reverse engineering skills while analyzing scraping target, experience in software architecture and design, writing clean, idiomatic Python code.


Your task consists of 2 stages:

## 1. Create scraper for TikTok products

- scraper must be always running and listen for product_ids from Redis queue;
- scraper must have support for HTTP proxies;
- scraper should be able to scrape thousands of products (you can find 10k example product_ids in `product_ids.json`);
- scraper must save product into Redis, including following data: id, url, price, images, title, description, variations, shipping info, specifications, scraping_time, proxy, etc.;
- would be BIG PLUS if you can also save product's related videos (advertisement);


## 2. Create API for operating scraped data

Goal is to demonstrate developer's experience with FastAPI, using routes, develop project structure, architecture.

- api must have an endpoint for writing items into scraping queue;
- api must have an endpoint for reading scraped data;
- any other secondary endpoints you think may be helpful are welcome;


You are free to use any tools you want for achieving the goal. Also, feel free to bump versions of libraries in Pipfile or add new ones, add new services in docker-compose, linters, etc. Anything you think will help to demonstrate your skills.

